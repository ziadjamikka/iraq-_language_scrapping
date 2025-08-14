# Scraping Report for Iraqi Arabic Dialect Datasets

## Overview

This report summarizes the findings from scraping various online sources for publicly accessible datasets, files, and links related to the Iraqi Arabic dialect. The initial search was based on the user's request to find and scrape data for the Iraqi dialect.

## Findings

### Academia.edu and ArXiv.org (Previous Attempt)

As previously reported, access to `academia.edu` was blocked due to `robots.txt` restrictions. From `arxiv.org`, the PDF of the paper "Lisan: Yemeni, Iraqi, Libyan, and Sudanese Arabic Dialect Copora with Morphological Annotations" was successfully downloaded. However, no direct dataset links were found on the arXiv page itself; only general links to platforms like Hugging Face and Papers with Code were present.

### GitHub Repository: ebady/Iraqi-Arabic-Dialect-Dataset

**URL:** `https://github.com/ebady/Iraqi-Arabic-Dialect-Dataset`

This repository contains a dataset for Iraqi Arabic Dialect (IA2D) for sentiment analysis. I successfully navigated the repository and downloaded the following text files:

*   `./downloads/Tweets_Raw_Data.txt`
*   `./downloads/Annotated_Dataset_After_Preprocessing.txt`
*   `./downloads/Annotated_Tweets_Before_Preprocessing.txt`

These files contain raw and preprocessed Iraqi Arabic tweets, which are directly relevant to the user's request.

### GitHub Repository: hayderkharrufa/iraqi-dialect-tts-corpus

**URL:** `https://github.com/hayderkharrufa/iraqi-dialect-tts-corpus`

This repository hosts a dataset for training a Text-to-Speech system focused on the Iraqi dialect. The dataset is hosted on Google Drive. I attempted to download the dataset, but encountered a Google Drive virus scan warning, and the file size (2.1 GB) exceeded the download limit (50 MB) set for this task. Therefore, the dataset was not downloaded.

### Kaggle Dataset: Arabic (Iraqi dialect) text classification dataset

**URL:** `https://www.kaggle.com/datasets/husseinnassrullah/arabic-iraqi-dialect-text-classification-dataset/data`

This dataset is for Arabic (Iraqi dialect) text classification. I attempted to download it, but Kaggle requires login or registration to access the dataset. As per the instructions, I did not attempt to bypass login walls.

## Discovered Links (from `links.json`)

```json
[
    {
        "url": "https://arxiv.org/pdf/2212.06468",
        "source_page": "https://arxiv.org/abs/2212.06468",
        "http_status": 200,
        "content_type": "application/pdf",
        "notes": ["Downloaded PDF: downloads/2212.06468"]
    },
    {
        "url": "https://huggingface.co/huggingface",
        "source_page": "https://arxiv.org/abs/2212.06468",
        "http_status": 200,
        "content_type": "text/html; charset=utf-8",
        "notes": []
    },
    {
        "url": "https://paperswithcode.com/",
        "source_page": "https://arxiv.org/abs/2212.06468",
        "http_status": 200,
        "content_type": "text/html; charset=utf-8",
        "notes": []
    },
    {
        "url": "https://scholar.google.com/scholar_lookup?arxiv_id=2212.06468",
        "source_page": "https://arxiv.org/abs/2212.06468",
        "http_status": 200,
        "content_type": "text/html; charset=UTF-8",
        "notes": []
    },
    {
        "url": "https://github.com/ebady/Iraqi-Arabic-Dialect-Dataset/blob/master/Data/Tweets_Raw_Data.txt",
        "source_page": "https://github.com/ebady/Iraqi-Arabic-Dialect-Dataset",
        "http_status": 200,
        "content_type": "text/plain; charset=utf-8",
        "notes": ["Downloaded text file: downloads/Tweets_Raw_Data.txt"]
    },
    {
        "url": "https://github.com/ebady/Iraqi-Arabic-Dialect-Dataset/blob/master/Data/Annotated_Dataset_After_Preprocessing.txt",
        "source_page": "https://github.com/ebady/Iraqi-Arabic-Dialect-Dataset",
        "http_status": 200,
        "content_type": "text/plain; charset=utf-8",
        "notes": ["Downloaded text file: downloads/Annotated_Dataset_After_Preprocessing.txt"]
    },
    {
        "url": "https://github.com/ebady/Iraqi-Arabic-Dialect-Dataset/blob/master/Data/Annotated_Tweets_Before_Preprocessing.txt",
        "source_page": "https://github.com/ebady/Iraqi-Arabic-Dialect-Dataset",
        "http_status": 200,
        "content_type": "text/plain; charset=utf-8",
        "notes": ["Downloaded text file: downloads/Annotated_Tweets_Before_Preprocessing.txt"]
    },
    {
        "url": "https://drive.google.com/file/d/1iQ-ueye2pLFavy-2HWDEOhscD_wn_7ie/view",
        "source_page": "https://github.com/hayderkharrufa/iraqi-dialect-tts-corpus",
        "http_status": 200,
        "content_type": "text/html; charset=utf-8",
        "notes": ["File too large to download (2.1GB)", "Google Drive virus scan warning"]
    },
    {
        "url": "https://www.kaggle.com/datasets/husseinnassrullah/arabic-iraqi-dialect-text-classification-dataset/data",
        "source_page": "https://www.kaggle.com/datasets/husseinnassrullah/arabic-iraqi-dialect-text-classification-dataset/data",
        "http_status": 200,
        "content_type": "text/html; charset=utf-8",
        "notes": ["Requires login/registration for download"]
    }
]
```

## Summary of Data Found

I successfully found and downloaded three text files containing Iraqi Arabic dialect data from the `ebady/Iraqi-Arabic-Dialect-Dataset` GitHub repository. These files are directly usable for text-based analysis.

Other potential sources were identified but could not be fully accessed due to `robots.txt` restrictions (Academia.edu), large file size/virus warnings (Google Drive link from `hayderkharrufa/iraqi-dialect-tts-corpus`), or login requirements (Kaggle).

## Next Suggested Steps

1.  **Review downloaded data:** Examine the downloaded text files from the `ebady/Iraqi-Arabic-Dialect-Dataset` to ensure they meet your specific needs for Iraqi Arabic dialect data.
2.  **Explore alternatives for large/restricted datasets:** If the downloaded data is insufficient, consider manually accessing the Kaggle dataset (if you have an account) or the Google Drive dataset (if you can handle large files and bypass the virus warning) outside of this environment.
3.  **Further targeted search:** If more data is needed, consider more specific searches for academic papers or projects that explicitly mention downloadable Iraqi Arabic dialect corpora or tools, focusing on university linguistic departments or research groups.


