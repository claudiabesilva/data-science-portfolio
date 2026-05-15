# Zomato Bangalore Restaurant Insights

Exploratory data analysis of **51,717 Bangalore restaurants** from Zomato, covering ratings, online ordering trends, customer review text mining, and geospatial density mapping.

## Overview

This project answers three main questions:

1. **Do restaurants that offer online ordering receive higher ratings?**
2. **What do customers talk about most in Quick Bites reviews?**
3. **Where are North Indian (and other cuisines) restaurants concentrated across Bangalore?**

## Key Findings

- Restaurants with online ordering are consistently rated higher — the share of online-ordering restaurants grows significantly above the 3.5 rating mark.
- The most frequent bigrams in Quick Bites reviews are *"really good"*, *"must try"*, and *"This place"*, reflecting overall positive sentiment.
- North Indian restaurants are most concentrated in **BTM** (2,469), **HSR** (1,123), and **Whitefield** (1,059).

## Project Structure

```
Zomato_Case_of_Study/
├── Zomato_Case_of_Study.ipynb   # Main analysis notebook
└── README.md
```

> **Note:** The raw dataset (`zomato_rawdata.sqlite`, ~575MB) is excluded from this repository.
> Download it from [Kaggle — Zomato Bangalore Restaurants](https://www.kaggle.com/datasets/himanshupoddar/zomato-bangalore-restaurants) and place it in this folder before running the notebook.

## Analysis Breakdown

### 1. Data Cleaning
- Loaded data from SQLite into pandas
- Cleaned the `rate` column: removed `'/5'` suffix, replaced `'NEW'` and `'-'` with `NaN`, converted to float
- Assessed and handled missing values across all columns (`dish_liked` had 54% missing — expected for user-generated data)

### 2. Online Ordering vs. Rating
- Built a cross-tabulation of rating × online order availability
- Normalized to percentage split per rating band
- Visualized with stacked bar charts

### 3. Review Text Mining (Quick Bites segment)
- Filtered for Quick Bites restaurant type (~25,000 restaurants)
- Tokenized reviews using NLTK `RegexpTokenizer` (alphabetic tokens only)
- Removed English stopwords + custom noise words (`rated`, `nan`, etc.)
- Performed **unigram**, **bigram**, and **trigram** frequency analysis with `FreqDist`

### 4. Geospatial Heatmap
- Geocoded 94 unique Bangalore neighborhoods using `geopy` / OpenStreetMap Nominatim
- Manually resolved 3 locations that the geocoder could not find
- Mapped restaurant density per neighborhood using `folium` HeatMap
- Built a reusable `get_heatmap(cuisine)` function — pass any cuisine string to generate a new map

## How to Run

1. Download the dataset from Kaggle and place `zomato_rawdata.sqlite` in this folder
2. Install dependencies:
   ```bash
   pip install pandas numpy matplotlib seaborn nltk geopy folium
   ```
3. Download NLTK data (first run only):
   ```python
   import nltk
   nltk.download('stopwords')
   ```
4. Open and run `Zomato_Case_of_Study.ipynb`

## Tools & Libraries

| Purpose | Library |
|---|---|
| Data manipulation | pandas, numpy |
| Visualization | matplotlib, seaborn |
| Text mining | NLTK |
| Geocoding | geopy (Nominatim) |
| Interactive maps | folium |
| Data source | sqlite3 |