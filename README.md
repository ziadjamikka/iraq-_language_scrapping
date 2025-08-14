# iraq-_language_scrapping
# Iraqi Arabic Dialect Dataset Scraping Project

## Overview

This project contains tools and datasets for scraping, processing, and analyzing Iraqi Arabic dialect text data from various online sources. The project focuses on collecting and organizing Iraqi Arabic dialect corpora for natural language processing and linguistic research.

## Project Files Description

### Core Scraping Scripts

#### `scrape_links.py`
- **Purpose**: Main web scraping script for extracting links and downloading datasets related to Iraqi Arabic dialects
- **Features**:
  - Respects robots.txt rules for ethical scraping
  - Downloads PDFs and text files up to 50MB
  - Handles various content types (PDF, text, HTML)
  - Includes rate limiting (1 request per second per domain)
  - Detects login/paywall requirements
  - Saves results to `links.json`
- **Dependencies**: `requests`, `urllib.parse`, `json`, `os`, `time`

### Data Files

#### `links.json`
- **Purpose**: Contains metadata about all scraped links and their processing results
- **Content**: JSON array with link information including:
  - URL and source page
  - HTTP status codes
  - Content types
  - Download notes and status
  - File size information
- **Sources**: Links from arXiv papers, GitHub repositories, Google Drive, and Kaggle datasets

#### `2212.06468`
- **Purpose**: Downloaded PDF from arXiv paper "Lisan: Yemeni, Iraqi, Libyan, and Sudanese Arabic Dialect Copora with Morphological Annotations"
- **Format**: Binary PDF file
- **Size**: Research paper discussing Arabic dialect corpora and annotation tools

### Iraqi Arabic Datasets

#### `Tweets_Raw_Data.txt`
- **Purpose**: Raw Iraqi Arabic tweets dataset
- **Content**: 1,673 lines of raw tweet data in Iraqi Arabic dialect
- **Format**: Tab-separated values with tweet numbers and text content
- **Source**: GitHub repository `ebady/Iraqi-Arabic-Dialect-Dataset`
- **Use Case**: Raw data for sentiment analysis and dialect studies

#### `Annotated_Dataset_After_Preprocessing.txt`
- **Purpose**: Preprocessed and annotated Iraqi Arabic tweets dataset
- **Content**: 1,171 lines of annotated tweets with sentiment labels
- **Format**: Semicolon-separated values with tweet ID, text, and sentiment (True/False/IDK/N)
- **Annotations**: Sentiment analysis labels for Iraqi Arabic text
- **Source**: GitHub repository `ebady/Iraqi-Arabic-Dialect-Dataset`
- **Use Case**: Training data for sentiment analysis models

#### `iraqi_iadd_cleaned.jsonl`
- **Purpose**: Cleaned Iraqi Arabic dataset in JSONL format for machine learning
- **Content**: 217 instruction-output pairs in Iraqi Arabic dialect
- **Format**: JSON Lines format with "instruction" and "output" fields
- **Content**: Various Iraqi Arabic expressions, conversations, and cultural content
- **Use Case**: Fine-tuning language models for Iraqi Arabic understanding

### Documentation

#### `Scraping Report for Iraqi Arabic Dialect Datasets.md`
- **Purpose**: Comprehensive report documenting the scraping process and findings
- **Content**: 
  - Overview of scraping methodology
  - Results from different sources (arXiv, GitHub, Google Drive, Kaggle)
  - Summary of successfully downloaded datasets
  - Analysis of access restrictions and limitations
  - Recommendations for future data collection
- **Use Case**: Reference document for understanding the data collection process

#### `todo.md`
- **Purpose**: Task list and notes for the project
- **Content**: Currently contains an error message related to image format processing
- **Status**: Needs review and cleanup

### Data Sources Identified

The scraping process identified several key sources for Iraqi Arabic dialect data:

1. **GitHub Repository**: `ebady/Iraqi-Arabic-Dialect-Dataset`
   - Successfully downloaded: Raw tweets, annotated dataset, preprocessed data
   - Focus: Sentiment analysis for Iraqi Arabic

2. **GitHub Repository**: `hayderkharrufa/iraqi-dialect-tts-corpus`
   - Content: Text-to-Speech corpus for Iraqi dialect
   - Status: File too large (2.1GB), Google Drive virus scan warning

3. **Kaggle Dataset**: Arabic (Iraqi dialect) text classification dataset
   - Content: Text classification data
   - Status: Requires login/registration

4. **Academic Sources**: arXiv paper 2212.06468
   - Content: Research on Arabic dialect corpora
   - Status: Successfully downloaded

## Project Structure

```
Scrape Iraqi Arabic Dataset Links from Two Pages/
├── scrape_links.py                    # Main scraping script
├── links.json                         # Scraping results and metadata
├── 2212.06468                        # Downloaded arXiv PDF
├── Tweets_Raw_Data.txt               # Raw Iraqi Arabic tweets
├── Annotated_Dataset_After_Preprocessing.txt  # Preprocessed tweets with labels
├── iraqi_iadd_cleaned.jsonl          # Cleaned dataset in JSONL format
├── Scraping Report for Iraqi Arabic Dialect Datasets.md  # Project documentation
├── todo.md                           # Task list and notes
└── README.md                         # This file
```

## Usage

### Running the Scraper

```bash
python scrape_links.py
```

The script will:
1. Process predefined links from various sources
2. Download accessible datasets
3. Save results to `links.json`
4. Create a `downloads/` directory for downloaded files

### Data Analysis

The collected datasets can be used for:
- Iraqi Arabic dialect research
- Sentiment analysis model training
- Natural language processing for Arabic dialects
- Linguistic studies of Iraqi Arabic
- Machine learning model fine-tuning

## Requirements

- Python 3.6+
- Required packages: `requests`
- Internet connection for web scraping
- Sufficient disk space for dataset downloads

## Ethical Considerations

- The scraper respects `robots.txt` files
- Implements rate limiting to avoid overwhelming servers
- Only downloads publicly accessible content
- Does not attempt to bypass login walls or paywalls

## Future Work

1. **Data Quality**: Implement data cleaning and validation
2. **Expanded Sources**: Identify additional Iraqi Arabic datasets
3. **Processing Pipeline**: Create automated data preprocessing workflows
4. **Model Training**: Develop models using the collected datasets
5. **Documentation**: Expand documentation and usage examples

## Contributing

This project is focused on collecting Iraqi Arabic dialect data for research purposes. Contributions should focus on:
- Improving data quality
- Adding new data sources
- Enhancing the scraping methodology
- Developing analysis tools

## License

This project is for research and educational purposes. Please respect the terms of use for all data sources and ensure compliance with relevant data protection regulations.
