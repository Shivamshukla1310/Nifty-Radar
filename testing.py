import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime

df = pd.DataFrame({
    "Date": pd.date_range("2024-01-01", periods=10),
    "Open": range(10),
    "High": [x+2 for x in range(10)],
    "Low": [x-1 for x in range(10)],
    "Close": [x+1 for x in range(10)]
})

fig = go.Figure(data=[go.Candlestick(
    x=df['Date'].dt.to_pydatetime(),
    open=df['Open'],
    high=df['High'],
    low=df['Low'],
    close=df['Close']
)])
st.plotly_chart(fig, use_container_width=True)
