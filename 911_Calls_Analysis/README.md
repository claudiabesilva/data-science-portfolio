# 911 Calls: Emergency Response Patterns in Montgomery County, PA

Exploratory analysis of **~99,500 emergency call records** from Montgomery County, PA, covering call reasons (EMS, Fire, Traffic), geographic distribution, and time-based patterns.

## Overview

This project answers three main questions:

1. **Where do 911 calls come from, and what are they for?**
2. **How does call volume change by hour, day of week, and month?**
3. **Are there recognizable patterns when day/hour and day/month are visualized together?**

## Key Findings

- EMS accounts for the largest share of calls (**49%**, 48,877 of 99,492), nearly matching Traffic (35,695) and Fire (14,920) combined.
- Lower Merion, Abington, Norristown, Upper Merion, and Cheltenham townships (zip codes in the **19401–19406** range) generate the highest call volumes.
- Call volume varies clearly by day of week, hour of day, and month — visible in heatmaps and clustermaps that group similar time periods together.

## Project Structure

```
911_Calls_Analysis/
├── 911_Calls_Analysis.ipynb   # Main analysis notebook
└── README.md
```

> **Note:** The raw dataset (`911.csv`, ~18MB) is excluded from this repository.
> Download it from [Kaggle — Montgomery County, PA 911 Calls](https://www.kaggle.com/mchirico/montcoalert) and place it in this folder before running the notebook.

## Analysis Breakdown

### 1. Data Overview
- Loaded 99,492 call records from CSV
- Inspected structure and missing values (`zip`, `twp`, `addr` all have some nulls)

### 2. Call Reason Extraction
- Parsed the `title` column (110 distinct codes) to extract a broader `Reason` category — EMS, Fire, or Traffic
- Visualized the reason breakdown with a count plot

### 3. Time-Based Feature Engineering
- Converted `timeStamp` from string to proper `datetime`
- Derived `Hour`, `Month`, and `Day of Week` columns
- Mapped numeric day-of-week values to names (Mon–Sun)

### 4. Trends Over Time
- Count plots of calls by day of week and month, split by reason
- Monthly and daily call volume trends (overall and per-reason)
- Linear fit across months to smooth out the trend

### 5. Heatmaps
- Restructured the data (day of week × hour, and day of week × month) using `groupby` + `unstack`
- Visualized call density with `seaborn` heatmaps and clustermaps

## How to Run

1. Download the dataset from Kaggle and place `911.csv` in this folder
2. Install dependencies:
   ```bash
   pip install pandas numpy matplotlib seaborn
   ```
3. Open and run `911_Calls_Analysis.ipynb`

## Tools & Libraries

| Purpose | Library |
|---|---|
| Data manipulation | pandas, numpy |
| Visualization | matplotlib, seaborn |
| Data source | CSV |

## Data Source

[Kaggle — Montgomery County, PA 911 Calls](https://www.kaggle.com/mchirico/montcoalert)
