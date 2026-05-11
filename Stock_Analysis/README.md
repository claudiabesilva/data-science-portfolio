# StockyAnalysis

StockyAnalysis is a Python-based stock market analysis project focused on technology companies from the S&P 500 dataset.  
It includes:

- an exploratory Jupyter notebook (`Stock_Analysis.ipynb`) for data investigation and visual analysis
- a Streamlit dashboard (`app.py`) for interactive stock exploration

The analysis currently centers on four companies: Apple (`AAPL`), Amazon (`AMZN`), Google (`GOOG`), and Microsoft (`MSFT`).

## Project Structure

`StockyAnalysis/`

- `Stock_Analysis.ipynb` - main notebook with exploratory analysis and visualizations
- `app.py` - Streamlit dashboard app
- `S&P_resources/individual_stocks_5yr/` - CSV files with historical stock data
- `S&P_resources/Stock_price_analysis_Shan_Singh.ipynb` - reference notebook

## Features

- Historical closing-price trend analysis
- Moving averages (10, 20, 50 days)
- Daily return calculation and visualization
- Monthly/quarterly/yearly resampling of close prices
- Correlation heatmap across selected tech stocks

## Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly Express
- Streamlit
- Jupyter Notebook

## Setup

1. Clone or open this project locally.
2. Create and activate a virtual environment (recommended).
3. Install dependencies:

```bash
pip install pandas numpy matplotlib seaborn plotly streamlit notebook
```

## Running the Notebook

From the project root:

```bash
jupyter notebook
```

Then open `Stock_Analysis.ipynb` and run cells in order.

## Running the Streamlit App

From the project root:

```bash
streamlit run app.py
```

## Important Path Note

`app.py` currently uses absolute paths that point to a local folder named `Stock_Analysis`.  
If you run the app on another machine or different folder layout, update `company_list` in `app.py` to use relative paths, for example:

```python
company_list = [
    "S&P_resources/individual_stocks_5yr/AAPL_data.csv",
    "S&P_resources/individual_stocks_5yr/AMZN_data.csv",
    "S&P_resources/individual_stocks_5yr/GOOG_data.csv",
    "S&P_resources/individual_stocks_5yr/MSFT_data.csv",
]
```

## Future Improvements

- Add a `requirements.txt` or `pyproject.toml`
- Add screenshots/GIF of the dashboard
- Add support for user-selected ticker lists
- Add risk metrics (volatility, drawdown, Sharpe ratio)

## Disclaimer

This project is for educational and portfolio purposes only and does not constitute financial advice.
