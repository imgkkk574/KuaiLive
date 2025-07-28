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
|  author_id         |                                           |       | 56006        |
|      gender        |                                           |       | M        |
|       age          |                                           |       | 24-30        |
|    country         |                                           |       | China        |
|      device_brand  |                                           |       | APPLE        |
|     device_price   |                                           |       | 5000+        |
| live_operation_tag |                                           |       |  Relationship       |
|      fans_user_num |                                           |       |  10000-100000       |
|fans_group_fans_num |                                           |       | 0-10        |
|   follow_user_num  |                                           |       |  1000-10000       |
|first_live_timestamp|                                           |       |  2018-02-04       |
|   accu_live_cnt    |                                           |       |  100-500       |
|  accu_live_duration|                                           |       | 500000000-1000000000        |
|   accu_play_cnt    |                                           |       |   100000-500000      |
|  accu_play_duration|                                           |       | 50000000000-100000000000        |
|   reg_timestamp    |                                           |       |   2014-07-03      |
|   onehot_feat0     |                                           |       |    1     |
|   onehot_feat1     |                                           |       |    0     |
|   onehot_feat2     |                                           |       |    0     |
|   onehot_feat3     |                                           |       |    0     |
|   onehot_feat4     |                                           |       |    0     |
|   onehot_feat5     |                                           |       |    0    |
|   onehot_feat6     |                                           |       |    0     |




#### 2. Descriptions of the fields in click.csv

| Field Name         | Description                               | Type  | Example |
| ------------------ | ----------------------------------------- | ----- | ------- |
|    user_id         |                                           |       |    8505 |
|   live_id          |                                           |       |9342705  |
|  author_id         |                                           |       | 392199  |
|   timestamp        |                                           |       | 1746374400022        |
| watch_live_time    |                                           |       |  2852   |




#### 3. Descriptions of the fields in comment.csv

| Field Name         | Description                               | Type  | Example |
| ------------------ | ----------------------------------------- | ----- | ------- |
|    user_id         |                                           |       |    23154 |
|   live_id          |                                           |       |7865151  |
|  author_id         |                                           |       | 433825  |
|   timestamp        |                                           |       | 1746374400819   |


#### 4. Descriptions of the fields in gift.csv


| Field Name         | Description                               | Type  | Example |
| ------------------ | ----------------------------------------- | ----- | ------- |
|    user_id         |                                           |       |    11504|
|   live_id          |                                           |       |6086847  |
|  author_id         |                                           |       | 114419  |
|   timestamp        |                                           |       | 1746374441260       |
| gift_price         |                                           |       |     2   |

#### 5. Descriptions of the fields in like.csv

| Field Name         | Description                               | Type  | Example |
| ------------------ | ----------------------------------------- | ----- | ------- |
|    user_id         |                                           |       |    5222 |
|   live_id          |                                           |       |541927   |
|  author_id         |                                           |       | 244121 |
|   timestamp        |                                           |       | 1746374414059 |


#### 6. Descriptions of the fields in mapped_room.csv

| Field Name         | Description                               | Type  | Example |
| ------------------ | ----------------------------------------- | ----- | ------- |
|     p_date         |                                           |       |20250525 |
|       live_id      |                                           |       |7336601  |
|      author_id     |                                           |       |   252634|
|      live_type     |                                           |       |   1     |
| start_timestamp    |                                           |       |1748131180878  |
|   end_timestamp    |                                           |       |1748275200000  |
|live_content_category|                                           |       |  shop       |
|   live_name_id     |                                           |       |  0      |



#### 7. Descriptions of the fields in title_embeddings.pca128.npz

| Field Name         | Description                               | Type  | Example |
| ------------------ | ----------------------------------------- | ----- | ------- |
|                    |                                           |       |         |
|                    |                                           |       |         |
|                    |                                           |       |         |

#### 8. Descriptions of the fields in user.csv

user_id,age,gender,country,device_brand,device_price,reg_timestamp,fans_num,follow_num,first_watch_live_timestamp,accu_watch_live_cnt,accu_watch_live_duration,is_live_author,is_photo_author,onehot_feat0,onehot_feat1,onehot_feat2,onehot_feat3,onehot_feat4,onehot_feat5,onehot_feat6
22733,18-23,M,China,DESKTOP,0,2023-05-03,0-10,10-100,2023-05-03,0-50000,0-1000000000,0,0,0,0,0,0,0,0,0

| Field Name         | Description                               | Type  | Example |
| ------------------ | ----------------------------------------- | ----- | ------- |
|                    |                                           |       |         |
|                    |                                           |       |         |
|                    |                                           |       |         |