---
title: "KuaiLive"
layout: default
sitemap: false
permalink: /detailed_statistics.html
---

[HOMEPAGE](./)

## Data Descriptions:

File organization:

```bash
  KuaiLive
  ├── author.csv          
  ├── click.csv
  ├── comment.csv
  ├── gift.csv
  ├── like.csv
  ├── mapped_room.csv
  ├── title_embeddings_pca128.npy
  └── user.csv
```

#### 1. Descriptions of the fields in author.csv

| Field Name         | Description                               | Type  | Example |
| ------------------ | ----------------------------------------- | ----- | ------- |
|  author_id         |    The ID of the author.                  | int64 | 56006        |
|      gender        |    The gender of the author.              |string | M        |
|       age          |    The age range of the author.           |string (range) | 24-30        |
|    country         | The country where the author resides.     | string| China        |
|      device_brand  |The brand of the device used by the author.| string| APPLE        |
|     device_price   |The price range of the device.             | string (range)      | 5000+        |
| live_operation_tag | The operational category of the author.   |string |  Relationship       |
|      fans_user_num | The number of users who have followed the author. |  string (range)     |  10000-100000       |
|fans_group_fans_num | The number of fans from the author's fans group.  |  string (range)     | 0-10        |
|   follow_user_num  | The number of users followed by the author.     |  string (range)     |  1000-10000       |
|first_live_timestamp|  The date when the author started their first live room.   |  timestamp     |  2018-02-04       |
|   accu_live_cnt    |  The total number of live rooms the author has hosted.   |  string (range)     |  100-500       |
|  accu_live_duration|  The cumulative duration of all live rooms, in milliseconds.    |  string(range)     | 500000000-1000000000        |
|   accu_play_cnt    |  The total number of times the author’s live rooms have been viewed.    | string (range)      |   100000-500000      |
|  accu_play_duration|  The cumulative duration of all live rooms, in milliseconds.     | string (range)      | 50000000000-100000000000        |
|   reg_timestamp    |  The date when the author registered on the platform.          |   timestamp    |   2014-07-03      |
|   onehot_feat0     |  A feature with binary values (e.g., 0 or 1).       |   int64    |    1     |
|   onehot_feat1     |  A feature with binary values (e.g., 0 or 1).       |   int64    |    0     |
|   onehot_feat2     |  A feature with binary values (e.g., 0 or 1).       |   int64    |    0     |
|   onehot_feat3     |  A feature with binary values (e.g., 0 or 1).       |   int64    |    0     |
|   onehot_feat4     |  A feature with binary values (e.g., 0 or 1).       |   int64    |    0     |
|   onehot_feat5     |  A feature with binary values (e.g., 0 or 1).       |   int64    |    0     |
|   onehot_feat6     |  A feature with binary values (e.g., 0 or 1).       |   int64    |    0     |




#### 2. Descriptions of the fields in click.csv

| Field Name         | Description                               | Type  | Example |
| ------------------ | ----------------------------------------- | ----- | ------- |
|    user_id         |    The id of the user.                    | int64 |    8505 |
|   live_id          |    The id of the live room.               | int64 |9342705  |
|  author_id         |    The id of the author.                  | int64 | 392199  |
|   timestamp        |The timestamp when this interaction occurred. | int64      | 1746374400022        |
| watch_live_time    | The user’s watch time for this interaction, in milliseconds.  |  int64     |  2852   |




#### 3. Descriptions of the fields in comment.csv

| Field Name         | Description                               | Type  | Example |
| ------------------ | ----------------------------------------- | ----- | ------- |
|    user_id         |      The id of the user.                  | int64 |    23154 |
|   live_id          |      The id of the live room.             | int64 |7865151  |
|  author_id         |       The id of the author.               | int64 | 433825  |
|   timestamp        | The timestamp when this interaction occurred. | int64   | 1746374400819   |


#### 4. Descriptions of the fields in gift.csv


| Field Name         | Description                               | Type  | Example |
| ------------------ | ----------------------------------------- | ----- | ------- |
|    user_id         |   The id of the user.                  | int64  |    11504|
|   live_id          |     The id of the live room.             | int64 |6086847  |
|  author_id         |        The id of the author.               | int64  | 114419  |
|   timestamp        |     The timestamp when this interaction occurred. | int64   | 1746374441260       |
| gift_price         |   The total price of gifts sent during this interaction.          |  int64     |     2   |

#### 5. Descriptions of the fields in like.csv

| Field Name         | Description                               | Type  | Example |
| ------------------ | ----------------------------------------- | ----- | ------- |
|    user_id         |       The id of the user.                  | int64  |   5222 |
|   live_id          |     The id of the live room.             | int64   |541927   |
|  author_id         |         The id of the author.               | int64   | 244121 |
|   timestamp        |     The timestamp when this interaction occurred. | int64  | 1746374414059 |


#### 6. Descriptions of the fields in mapped_room.csv

| Field Name         | Description                               | Type  | Example |
| ------------------ | ----------------------------------------- | ----- | ------- |
|     p_date         |      The date of the live room.           | int64 |20250525 |
|       live_id      |           The id of the live room.        | int64   |7336601  |
|      author_id     |           The id of the author.           | int64    |   252634|
|      live_type     |  The type the live room, represented as a categorical code.   |   int64    |   1     |
| start_timestamp    |  The start time of the live room.         |  int64  |1748131180878  |
|   end_timestamp    | The end time of the live room.         |  int64  |1748275200000  |
|live_content_category|  The content category of the live room.      |  string     |  shop       |
|   live_name_id     |    The id associated with the live room title.         |    int64   |  0      |



#### 7. Descriptions of the fields in title_embeddings.pca128.npz

| Field Name         | Description                               | Type  | Example |
| ------------------ | ----------------------------------------- | ----- | ------- |
|                    |                                           |       |         |
|                    |                                           |       |         |
|                    |                                           |       |         |

#### 8. Descriptions of the fields in user.csv

| Field Name         | Description                               | Type  | Example |
| ------------------ | ----------------------------------------- | ----- | ------- |
|   user_id          |    The ID of the user.                    | int64 |  22733  |
|   age              |    The age range of the user.             | string (range)    |  18-23  |
|  gender            |   The gender of the user.                 | string|   M     |
|  country           |  The country where the user resides.      | string|  China  |
|  device_brand      | The brand of the device used by the user. | string| DESKTOP |
|  device_price      | The price range of the device.            | string (range)  |   0     |
|  reg_timestamp     |  The date when the user registered on the platform.|  timestamp   |2023-05-03|
|   fans_num         | The number of fans who have followed the user.  | string (range)      | 0-10    |
|   follow_num       | The number of users followed by the user.       | string (range)      | 10-100  |
|first_watch_live_timestamp| The date when the user first watched a live room. |  timestamp     |2023-05-03|
|accu_watch_live_cnt |  The total number of live rooms the user has watched.  |   string (range)    |0-50000  |
|accu_watch_live_duration| The cumulative duration of all live rooms the user has watched, in milliseconds.           |string (range)       |0-1000000000 |
| is_live_author     |  A binary indicator showing whether the user is a live author (1 = yes, 0 = no).   |  int64     |  0      |
| is_photo_author    |  A binary indicator showing whether the user is a photo content author (1 = yes, 0 = no).        |   int64    |   0     |
|   onehot_feat0     |  A feature with binary values (e.g., 0 or 1).       |   int64    |    0     |
|   onehot_feat1     |  A feature with binary values (e.g., 0 or 1).       |   int64    |    0     |
|   onehot_feat2     |  A feature with binary values (e.g., 0 or 1).       |   int64    |    0     |
|   onehot_feat3     |  A feature with binary values (e.g., 0 or 1).       |   int64    |    0     |
|   onehot_feat4     |  A feature with binary values (e.g., 0 or 1).       |   int64    |    0     |
|   onehot_feat5     |  A feature with binary values (e.g., 0 or 1).       |   int64    |    0     |
|   onehot_feat6     |  A feature with binary values (e.g., 0 or 1).       |   int64    |    0     |