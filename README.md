# KuaiComt

*KuaiComt* is a comprehensive short video recommendation dataset that includes abundant comment text and interaction data. It contains real user behavior logs collected from the short-video mobile app [Kuaishou](https://www.kuaishou.com/en), a leading short video app in China with over 400 million daily active users. On average, users spend over 120 minutes on the app each day, with more than 7 minutes (over 5%) spent in the video comments section. The comments section boasts a UV penetration rate of over 60%.

**This is the first recommendation dataset that not only records item text and interaction data but also includes abundant comment text and interaction data!**


## Overview

The following figure provides an example of the dataset. When users enter the app, they can scroll up and down to browse different videos. Additionally, users can click the comment button on the right side of the video to enter the comments section, where they can scroll through comments and engage in interactive behaviors such as likes and replies.


![kuaidata](./assets/fig/example.png)

## Download the data:

KuaiComt has been shared at [https://zenodo.org/records/13922581](https://zenodo.org/records/13922581).

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.13922581.svg)](https://doi.org/10.5281/zenodo.13922581)

According to our company's data sharing policy, our datasets are made available through confidentiality agreements. 

> In compliance with the recently enacted **Personal Information Protection Law** and **Data Security Assessment Measures for Cross-Border Data Transfer in China**, we currently provide datasets exclusively to Chinese entities (universities, research institutes, and companies).

> You are required to send us your **name** and **institutional details**, after which we will provide you with the relevant confidentiality agreement. The dataset will be shared with you only after the agreement has been signed.


OPTION 1. Download via your browser:

You can download the dataset from this [link](https://zenodo.org/records/13922581).

OPTION 2: Download via the 'wget' command tool:

For the **KuaiComt** dataset:
```bash
wget https://zenodo.org/record/13922581/files/KuaiComt.zip

unzip KuaiComt.zip
```

## Citation

If you find our dataset useful, please cite the paper:

```
@inproceedings{zhang2025comment,
  title={Comment Staytime Prediction with LLM-enhanced Comment Understanding},
  author={Zhang, Changshuo and Lin, Zihan and Liu, Shukai and Liu, Yongqi and Li, Han},
  booktitle={Companion Proceedings of the ACM on Web Conference 2025},
  pages={586--595},
  year={2025}
}
```

## License

[![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg

