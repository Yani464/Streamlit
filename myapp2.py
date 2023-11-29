import yfinance as yf
import streamlit as st

st.write("""
# Цена акций компании Apple за последние 10 лет

Показаны **цена за акцию** и **дивиденды на одну акцию** компании Apple!

""")

tickerSymbol = 'AAPL'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2013-11-27', end='2023-11-27')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## Цена за одну акцию
""")
st.line_chart(tickerDf.Close)
st.write("""
## Дивиденды на одну акцию
""")
st.line_chart(tickerDf.Dividends)
st.write("""
## Обьем торгов за день
""")
st.line_chart(tickerDf.Volume)
