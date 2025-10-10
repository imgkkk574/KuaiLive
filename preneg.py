import pandas as pd
import ast
from tqdm import tqdm
from bisect import bisect_right

room_df = pd.read_csv('room.csv')
room_df = room_df[['live_id', 'author_id', 'start_timestamp', 'end_timestamp']]

author_room_map = {}
for _, row in tqdm(room_df.iterrows(), total=len(room_df), desc="Preprocessing room data"):
    author_id = row['author_id']
    entry = (row['start_timestamp'], row['end_timestamp'], row['live_id'])
    author_room_map.setdefault(author_id, []).append(entry)

for k in author_room_map:
    author_room_map[k].sort()

match_cache = {}

def map_author_time_to_live_id(author_id, timestamp):
    key = (author_id, timestamp)
    if key in match_cache:
        return match_cache[key]

    rooms = author_room_map.get(author_id, [])
    starts = [r[0] for r in rooms]
    idx = bisect_right(starts, timestamp) - 1
    if idx >= 0 and rooms[idx][0] <= timestamp < rooms[idx][1]:
        live_id = rooms[idx][2]
        match_cache[key] = live_id
        return live_id

    match_cache[key] = None
    return None


def process_file(path, output_path, is_train=True):
    df = pd.read_csv(path, sep='\t')

    new_item_ids = []
    new_neg_items_list = []

    for _, row in tqdm(df.iterrows(), total=len(df), desc=f"Processing {path}"):
        author_id = row['item_id']
        timestamp = row['time']
        live_id = map_author_time_to_live_id(author_id, timestamp)
        if live_id is None:
            print(f"[WARN] No live_id found for item_id={author_id}, time={timestamp}")
            live_id = -1
        new_item_ids.append(live_id)

        if not is_train:
            neg_authors = ast.literal_eval(row['neg_items'])
            neg_live_ids = []
            for neg_author in neg_authors:
                neg_live_id = map_author_time_to_live_id(neg_author, timestamp)
                if neg_live_id is not None:
                    neg_live_ids.append(neg_live_id)
                else:
                    neg_live_ids.append(0)
                    print(f"[WARN] No live_id found for neg_item author_id={neg_author}, time={timestamp}")
            new_neg_items_list.append(str(neg_live_ids))

    df['item_id'] = new_item_ids
    if not is_train:
        df['neg_items'] = new_neg_items_list

    df.to_csv(output_path, sep='\t', index=False)

process_file(f'train.csv', 'train.csv', is_train=True)
process_file(f'dev.csv', 'dev.csv', is_train=False)
process_file(f'test.csv', 'test.csv', is_train=False)
