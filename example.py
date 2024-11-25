import yfinance as yf
import customyfinance as cf
from streamlit_extras.stylable_container import stylable_container

LongName = input("Enter a stock: ")
queryresponse = cf.QueryTicker(LongName)
for quote in queryresponse["quotes"]:
    if "longname" in quote:
        if quote["longname"].startswith(LongName):
            TickerID = quote["symbol"]

minasx = yf.Ticker(TickerID)
print(minasx.info)


###### - Custom Card
with stylable_container(
    key="container_with_border",
    css_styles="""
        {
            border: 1px solid rgba(49, 51, 63, 0.2);
            border-radius: 0.5rem;
            padding: calc(1em - 1px);
            background-color: #262731
        }
        """,
):
    st.markdown("This is a container with a border.")
