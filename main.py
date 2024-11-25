import streamlit as st
import yfinance as yf
from streamlit_card import card

import customyfinance as cf

st.write("# Maven")
col1, col2 = st.columns(2)
ticker = st.text_input(
    "ticker", placeholder="Search for a stock:", label_visibility="collapsed"
)
# addButtonIsCliked = col2.button("Search")

try:
    if cf.is_not_null_or_whitespace(ticker):
        queryResponse = cf.QueryTicker(f"{ticker}")
        for quote in queryResponse["quotes"]:
            if "longname" in quote:
                with st.container(border=True):
                    st.header(f"{quote["longname"]}")
                    col1, col2 = st.columns(2)
                    col1.text(f"{quote["symbol"]}")
                    col2.button("Select", key=f"{quote["symbol"]}")
                    # st.line_chart(data)

except Exception as e:
    st.write(f"An error occued: {e}")
