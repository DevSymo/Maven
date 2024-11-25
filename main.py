import streamlit as st
from streamlit_card import card

st.write("# Maven")
col1, col2 = st.columns(2)
website = col1.text_input("website", placeholder="Enter a website:", label_visibility="collapsed")
addButtonIsCliked = col2.button("Add")
card(
    title="Streamlit Card",
    text="This is a streamlit card!",
    styles={
        "card": {
            "width": "100%"
        },
        "filter": {
            # F0F2F6
            "background-color": "#262731"
        }
    }
)
