# Data Analysis Portfolio

A collection of data analysis and data science projects built to develop and demonstrate practical skills across the full analytics workflow — from data cleaning and exploration to NLP, geospatial analysis, and interactive dashboards.

> This portfolio is actively growing. New projects are added regularly.

## Projects

### [911 Calls: Emergency Response Patterns](911_Calls_Analysis/)
Exploratory analysis of ~99,500 emergency call records from Montgomery County, PA.
- Call reason extraction (EMS, Fire, Traffic) from raw title codes
- Time-based feature engineering: hour, day of week, month
- Day/hour and day/month heatmaps and clustermaps of call density

`pandas` `numpy` `matplotlib` `seaborn`

---

### [Zomato Bangalore Restaurant Insights](Zomato_Case_of_Study/)
Exploratory analysis of 51,700+ Bangalore restaurants from Zomato.
- Online ordering vs. rating relationship
- NLP review mining: unigram, bigram, and trigram frequency analysis
- Interactive geospatial heatmap of restaurant density by cuisine type

`pandas` `sqlite3` `NLTK` `geopy` `folium`

---

### [YouTube Trending Video Analysis](YoutubeCaseStudy/)
End-to-end analysis of YouTube trending data across 10 countries (~340K videos).
- Comment sentiment scoring with NLTK VADER + word clouds
- Emoji frequency analysis across the full comment dataset
- Category, channel, and engagement rate breakdowns

`pandas` `NLTK` `wordcloud` `emoji` `plotly` `SQLAlchemy`

---

### [S&P 500 Stock Analysis](Stock_Analysis/)
Historical stock market analysis of tech companies from the S&P 500, with an interactive dashboard.
- Closing price trends and moving averages (10, 20, 50 days)
- Daily returns, correlation heatmap, and resampling
- Streamlit dashboard for interactive exploration

`pandas` `matplotlib` `seaborn` `plotly` `Streamlit`

---

### [ChatGPT Data Analysis](chatgpt/)
Exploratory analysis of ChatGPT-related data.

`pandas` `matplotlib`

---

## Skills Demonstrated

| Area | Tools |
|---|---|
| Data wrangling | pandas, numpy, sqlite3, SQLAlchemy |
| Visualization | matplotlib, seaborn, plotly, folium |
| NLP & Text mining | NLTK (VADER, FreqDist, tokenization), wordcloud |
| Geospatial analysis | geopy, folium |
| Interactive dashboards | Streamlit |
| Data formats | CSV, JSON, SQLite |

## About

I'm transitioning into data analysis and science, using these projects to build hands-on experience with real-world datasets. Each project tackles a different domain and toolset, from restaurant reviews to financial markets to social media.
