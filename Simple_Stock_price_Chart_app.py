import yfinance as yf
import streamlit as st
st.write("""
# Simple Stock Price App
Shown are the stock closing price and volume of Google!
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
#get data on this ticker
tickerData = yf.Ticker('GOOGL')
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2023-1-30')
# Open	High	Low	Close	Volume	Dividends	Stock Splits
st.write(""" 
### Google Stock Price Column
""")
st.write(tickerDf)
st.write("""
### Google Closed Stock Pricefor the day
	""")
st.line_chart(tickerDf['Close'])
st.write("""
### Google Volume 
""")
st.line_chart(tickerDf['Volume'])
st.write("""
### Google Stock Open Price 
""")
st.line_chart(tickerDf['Open'])
st.write("""
### Google Stock High Price for the day 
""")
st.line_chart(tickerDf['High'])
