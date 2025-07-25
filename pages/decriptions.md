---
title: "KuaiComt"
layout: default
sitemap: false
permalink: /detailed_statistics.html
---

[HOMEPAGE](./)

## Data Descriptions:

File organization:

```bash
  KuaiComt
  ├── user_video_inter.csv          
  ├── user_comment_inter.csv
  ├── user_features.csv
  ├── video_features.csv
  └── comment_features.csv
```

#### 1. Descriptions of the fields in user_video_inter.csv

| Field Name        | Description                                                  | Type    | Example       |
| ----------------- | ------------------------------------------------------------ | ------- | ------------- |
| user_id           | The ID of the user.                                          | int64   | 2924305332    |
| video_id          | The ID of the viewed video.                                  | int64   | 110378652104  |
| p_hourmin         | The time of this interaction (format: HHSS).                 | int64   | 1500          |
| time_ms           | Unix timestamp (millisecond).                                | float64 | 1696141175214 |
| is_click          | Whether the user clicks the video.                           | int64   | 0             |
| is_like           | Whether the user likes the video.                            | int64   | 0             |
| is_follow         | Whether the user follows the author of the video.            | int64   | 0             |
| is_comment        | Whether the user comments the video.                         | int64   | 0             |
| is_forward        | Whether the user forwards the video.                         | int64   | 0             |
| is_collect        | Whether the user collects the video.                         | int64   | 0             |
| is_hate           | Whether the user hates the video.                            | int64   | 0             |
| long_view         | A binary feedback signal. It equals 1 when: `play_time_ms >= duration_ms if duration_ms <= 18,000 ms`, or `play_time_ms >=18,000 ms if duration_ms > 18,000 ms`. | int64   | 0             |
| play_time_ms      | The duration this video(item) has been played by this user (millisecond). | float64 | 5822          |
| duration_ms       | The total duration of this video (millisecond).              | float64 | 19960         |
| profile_stay_time | The time that the user stayed in this author’s profile.      | int64   | 0             |
| comment_stay_time | The time that the user stayed in the comments section of this video | int64   | 0             |


#### 2. Descriptions of the fields in user_comment_inter.csv

| Field Name             | Description                                                               | Type      | Example          |
| ---------------------- | ------------------------------------------------------------------------- | --------- | ---------------- |
| user_id                | The ID of the user.                                                       | int64     | 358692597   |
| comment_id | The ID of the comment.                                 | int64     | 455709716918    |
| time_stamp | Unix timestamp (second).                                            | int64 | 1696421927 |
| photo_id         | The ID of the video. | int64 | 65137995197 |
| is_like    | Whether the user likes the comment. | int64 | 1      |
| is_reply | Whether the user replies to the comment. | int64 | 0 |

#### 3. Descriptions of the fields in user_features.csv

| Field Name      | Description                                       | Type  | Example     |
| --------------- | ------------------------------------------------- | ----- | ----------- |
| user_id         | The ID of the user.                               | int64 | 1905604649 |
| user_active_degree | In the set of {‘high_active’, ‘full_active’, ‘middle_active’, ‘UNKNOWN’}. | str | "high_active" |
| is_live_author | Is this user a live author？ | int64 | 0 |
| produce_video_num | The number of produced videos by this user. | int64 | 1 |
| follow_count | The number of users that this user follows. | int64 | 274 |
| follow_user_num_range | The range of the number of users that this user follows. In the set of {‘0’, ‘(0,10]’, ‘(10,50]’, ‘(100,150]’, ‘(150,250]’, ‘(250,500]’, ‘(50,100]’, ‘500+’} | str | "(250,500]" |
| fans_count | The number of the fans of this user. | int64 | 676 |
| fans_user_num_range | The range of the number of fans of this user. In the set of {‘0’, ‘[1,10)’, ‘[10,100)’, ‘[100,1k)’, ‘[1k,5k)’, ‘[5k,1w)’, ‘[1w,10w)’} | str | "[100,1k)" |
| friend_user_num_range | The range of the number of friends that this user has. In the set of {‘0’, ‘[1,5)’, ‘[5,30)’, ‘[30,60)’, ‘[60,120)’, ‘[120,250)’, ‘250+’} | str | "250+" |
| register_days | The days since this user has registered. | int64 | 1252 |
| onehot_feat0 | An encrypted feature of the user. Each value indicates the position of “1” in the one-hot vector. Range: {0,1} | int64 | 1 |
| onehot_feat1 | An encrypted feature. Range: {0, 1, ..., 6} | int64 | 1 |
| onehot_feat2 | An encrypted feature. Range: {0, 1, ..., 54} | int64 | 14 |
| onehot_feat3 | An encrypted feature. Range: {0, 1, ..., 1685} | int64 | 898 |
| onehot_feat4 | An encrypted feature. Range: {0, 1, ..., 5} | int64 | 5 |
| onehot_feat5 | An encrypted feature. Range: {0, 1, ..., 9} | int64 | 0 |
| onehot_feat6 | An encrypted feature. Range: {0, 1, 2} | int64 | 2 |
| onehot_feat7 | An encrypted feature. Range: {0, 1, ..., 52} | int64 | 27 |
| onehot_feat8 | An encrypted feature. Range: {0, 1, ..., 391} | int64 | 153 |
| onehot_feat9 | An encrypted feature. Range: {0, 1, ..., 6} | int64 | 3 |
| onehot_feat10 | An encrypted feature. Range: {0, 1, ..., 4} | int64 | 3 |
| onehot_feat11 | An encrypted feature. Range: {0, 1, ..., 6} | int64 | 1 |
| onehot_feat12 | An encrypted feature. Range: {0, 1} | int64 | 0 |
| onehot_feat13 | An encrypted feature. Range: {0, 1} | int64 | 0 |
| onehot_feat14 | An encrypted feature. Range: {0, 1} | int64 | 0 |
| onehot_feat15 | An encrypted feature. Range: {0, 1} | int64 | 0 |
| onehot_feat16 | An encrypted feature. Range: {0, 1} | int64 | 0 |
| onehot_feat17 | An encrypted feature. Range: {0, 1} | int64 | 0 |
| onehot_feat18 | An encrypted feature. Range: {0, 1} | int64 | 0 |
| onehot_feat19 | An encrypted feature. Range: {0, 1} | int64 | 0 |
| onehot_feat20 | An encrypted feature. Range: {0, 1, ..., 4} | int64 | 2 |


#### 4. Descriptions of the fields in video_features.csv


| Field Name         | Description                               | Type  | Example |
| ------------------ | ----------------------------------------- | ----- | ------- |
| video_id       | The ID of the video.                  | int64 | 107291063430 |
| author_id | The ID of the author of this video. | int64 | 3087318004 |
| video_type | Type of this video (NORMAL or AD). | str | "NORMAL" |
| upload_dt | Upload date of this video. | str | "2023-07-06" |
| caption | The caption text of this video | str | "所以，怎么会没有遗憾呢#张睿  #李晟  #花非花雾非雾" |
| duration | The time duration of this duration (in milliseconds). | float | 36200.0 |
| category | Category of this video | str | "明星娱乐" |



#### 5. Descriptions of the fields in comment_features.csv

| Field Name                   | Description                                                      | Type      | Example     |
| ---------------------------- | ---------------------------------------------------------------- | --------- | ----------- |
| comment_id               | The ID of the comment.                                       | int64     | 681190728207 |
| comment_content        | The comment content text of this comment. | str   | "乱了、猫还怕老鼠[捂脸]" |
| video_id        | The ID of the video.                      | int64 | 107255530819             |
| comment_like_cnt     | The number of likes of this comment       | int64 | 112                      |
| comment_reply_out | The number of replies of this comment     | int64 | 6                        |
| show_comment_cnt_td | The number of shows of this comment.      | int64 | 645                      |
