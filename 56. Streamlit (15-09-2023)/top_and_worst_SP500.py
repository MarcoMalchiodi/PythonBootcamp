import yfinance as yf
import pandas as pd
import streamlit as st
from pandas.tseries.offsets import DateOffset,BDay


tickers = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0].Symbol

st.set_page_config(layout='wide')

@st.cache_data
def getdata():
    df = yf.download(tickers.to_list(),start='2020-01-01')
    df = df['Close']
    return df


df = getdata()
df.index = pd.to_datetime(df.index)

st.title('Index component performance of the S&P500')

n = st.number_input('Please provide the performance horizon in months: ',min_value=1,max_value=24)


def get_ret(df,n):
    previous_prices = df[:df.index[-1] - DateOffset(months=n)].tail(1).squeeze() # the sequeeze function turns a DataFrame into a Series
    recent_prices = df.loc[df.index[-1]]
    ret_df = recent_prices/previous_prices - 1
    return previous_prices.name,ret_df


date, ret_df = get_ret(df,n)

winners,losers = ret_df.nlargest(10),ret_df.nsmallest(10)
winners.name,losers.name = 'winners','losers'


print('winners & Losers')
st.table(winners)
st.table(losers)

winnerpick = st.selectbox('Pick a winner to visualize: ', winners.index)
st.line_chart(df[winnerpick][date:])

loserpick = st.selectbox('Pick a loser to visualize: ', losers.index)
st.line_chart(df[loserpick][date:])
