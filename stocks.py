import streamlit as st
import utilities as ut
import datetime as dt
import visualisation as vis

def app():
    #title of the web app
    st.title("Stocks Predictions")
    
    st.sidebar.subheader("Parameters")
    start_date = st.sidebar.date_input("Start date", dt.date(2015, 1, 1))
    end_date = st.sidebar.date_input("End date", dt.date.today())
    ticker_list = ut.getTickers()
    tickerSymbol = st.sidebar.selectbox('Coin', ticker_list) # Select ticker symbol
    
    
    # Fetch data
    df = ut.getTickerData("AAPL",start_date=start_date,end_date=end_date,interval='1d')
    st.write(df)
    fig = vis.plotTockenData(df=df, name=tickerSymbol,title="Chart")
    fig = fig.iplot(asFigure=True)
    
    st.plotly_chart(fig)    