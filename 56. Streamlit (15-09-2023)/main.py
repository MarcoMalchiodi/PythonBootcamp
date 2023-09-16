import pandas as pd
import yfinance as yf
import streamlit as st

st.title('Lit Finance Dashboard')

tickers = ('TSLA','AAPL','MSFT','BTC-USD','ETH-USD')

dropdown_menu = st.multiselect(label='Pick your assets:',options=tickers)

start = st.date_input(label='Start',value=pd.to_datetime('2021-01-01'))
end = st.date_input(label='End',value=pd.to_datetime('today'))

def cumulative_returns(df):
    rel = df.pct_change()
    cumret = (1+rel).cumprod() -1
    cumret = cumret.fillna(0)
    return cumret


if len(dropdown_menu) > 0:
    df = cumulative_returns(yf.download(dropdown_menu,start,end)['Adj Close'])

    st.line_chart(df)
