# -*- coding: utf-8 -*-
"""
Dashboard for showing the results of stocks
"""


# Importing packages
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import plotly.express as px

import streamlit as st


company_list = [
    '/Users/claudinha/Portfolio/Stock_Analysis/S&P_resources/individual_stocks_5yr/AAPL_data.csv',
    '/Users/claudinha/Portfolio/Stock_Analysis/S&P_resources/individual_stocks_5yr/AMZN_data.csv',
    '/Users/claudinha/Portfolio/Stock_Analysis/S&P_resources/individual_stocks_5yr/GOOG_data.csv',
    '/Users/claudinha/Portfolio/Stock_Analysis/S&P_resources/individual_stocks_5yr/MSFT_data.csv',
]

# Reading all the files in the list
all_data = pd.DataFrame()

for file in company_list:
    df = pd.read_csv(file)
    all_data = pd.concat([all_data, df], ignore_index=True)

# Date has to be converted to datetime
all_data['date'] = pd.to_datetime(all_data['date'])

tech_list = all_data['Name'].unique()


st.set_page_config(page_title = 'Stock analysis dashboard', layout = 'wide')

st.title('Tech stocks analysis dashboard')

st.sidebar.title('Choose a company')

selected_company = st.sidebar.selectbox('Select a stock', tech_list)

company_df = all_data[all_data['Name'] == selected_company]

company_df.sort_values('date')

## 1st plot

st.subheader(f'1. Closing price of {selected_company} over time')

fig1 = px.line(company_df, x = 'date', y = 'close',
               title = selected_company + ' closing price over time')

st.plotly_chart(fig1, use_container_width = True)


## 2nd plot
st.subheader('2. Moving averages [10, 20, 50 days]')

# Creating new columns witht the moving average for different windows
ma_day = [10, 20, 50] #moving average interval of days

for ma in ma_day:
    company_df['close_'+str(ma)] = company_df['close'].rolling(ma).mean()

fig2 = px.line(company_df, x = 'date', y = ['close','close_10','close_20','close_50'],
               title = selected_company + ' closing prices with moving average')

st.plotly_chart(fig2, use_container_width = True)

## 3rd plot
st.subheader('3. Daily returns for ' + selected_company)

# Creating the Daily return column for the percentual change beteween the current and the prior element
company_df['Daily return (in %)'] = company_df['close'].pct_change()*100

fig3 = px.line(company_df, x = 'date', y = 'Daily return (in %)',
               title = 'Daily return (in %)')
st.plotly_chart(fig3, use_container_width = True)

## 4th plot
st.subheader('4. Resampled closing price (Monthly/Quartely/Yearly)')

# Creating the Daily return column for the percentual change beteween the current and the prior element
company_df['Daily return (in %)'] = company_df['close'].pct_change()*100

# Setting the index to be the date
company_df.set_index('date', inplace = True)

resample_option = st.radio('Select resample frequency', ['Monthly', 'Quartely', 'Yearly'])

if resample_option == 'Monthly':
    resampled = company_df['close'].resample('ME').mean()
if resample_option == 'Quartely':
    resampled = company_df['close'].resample('QE').mean()
if resample_option == 'Yearly':
   resampled =  company_df['close'].resample('YE').mean()
      
fig4 = px.line(resampled,
               title = selected_company + ' ' + resample_option + ' ' + 'average closing price')
st.plotly_chart(fig4, use_container_width = True)


## 5th plot

# Reshaping the data so that each company becomes a separate time series,
# with dates as the index and closing prices as values
prices = all_data.pivot_table(
    index='date',
    columns='Name',
    values='close'
)

fig5, ax = plt.subplots()
sns.heatmap(prices.corr(), annot = True, cmap = 'coolwarm', ax = ax)
ax.set_xlabel('')
ax.set_ylabel('')
st.pyplot(fig5)

st.markdown('______')
st.markdown('**Note** This dashborad provides bacsic techinical analysis of major tech stocks using Python and Streamlit')



