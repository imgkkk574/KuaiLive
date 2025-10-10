import pandas as pd

df = pd.read_csv('click.csv')

df = df.rename(columns={'author_id': 'item_id', 'timestamp': 'time'})

df = df.sort_values(by=['user_id', 'time'])

train_rows = []
val_rows = []
test_rows = []

for user_id, group in df.groupby('user_id'):
    group = group.sort_values(by='time')
    if len(group) >= 2:
        test_rows.append(group.iloc[-1][['user_id', 'item_id', 'time']])
        val_rows.append(group.iloc[-2][['user_id', 'item_id', 'time']])
        train_rows.extend(group.iloc[:-2][['user_id', 'item_id', 'time']].to_dict(orient='records'))
    elif len(group) == 1:
        test_rows.append(group.iloc[-1][['user_id', 'item_id', 'time']])

train_df = pd.DataFrame(train_rows)
val_df = pd.DataFrame(val_rows)
test_df = pd.DataFrame(test_rows)

train_df.to_csv('train.csv', sep='\t', index=False)
val_df.to_csv('dev.csv', sep='\t', index=False)
test_df.to_csv('test.csv', sep='\t', index=False)
