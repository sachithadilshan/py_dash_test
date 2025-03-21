import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(
    page_title="CBS Test Dashboard",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded")

df = pd.read_csv("data/exchange_rate_usd_eur_aud.csv")
df['Date']=pd.to_datetime(df['Date'])

with st.sidebar:
    st.title('🏂 CBS Dashboard')
    
    year_list = list(df['Date'].dt.year.unique())
    
    selected_year = st.selectbox('Select a year', year_list)

st.write("Hello world")



plt.figure(figsize=(12,6))
plt.plot(df.index, df['USD'], label='USD')
plt.plot(df.index, df['EUR'], label='EUR')
plt.plot(df.index, df['AUD'], label='AUD')
plt.xlabel("Year")
plt.ylabel("Exchange Rate")
plt.title("Exchange Rate Trends Over 10 Years")
plt.legend()
st.pyplot(plt)


year_list = list(df['Date'].dt.year.unique())
selected_year1 = st.selectbox('Select year 1', year_list)
selected_year2 = st.selectbox('Select year 2', year_list)

currency_list = ['USD', 'EUR', 'AUD']

selected_currency = st.selectbox('Select currency', currency_list)

start1 = f"{selected_year1}-01-01"
end1 = f"{selected_year1}-12-31"

start2 = f"{selected_year2}-01-01"
end2 = f"{selected_year2}-12-31"



date_range_23 = pd.date_range(start1, end1)
date_range_24 = pd.date_range(start2, end2)



df = df.sort_values('Date')
df.set_index('Date', inplace=True)

df23 = df[df.index.isin(date_range_23)].reset_index()[selected_currency]
df24 = df[df.index.isin(date_range_24)].reset_index()[selected_currency]

plt.figure(figsize=(12,6))
plt.plot(df23.index, df23, label=f"{selected_year1}")
plt.plot(df24.index, df24, label=f"{selected_year2}")
plt.xlabel("Date")
plt.ylabel("Exchange Rate")
plt.title(f"Exchange Rate Trends for {selected_currency} between {selected_year1} and {selected_year2}")
plt.legend()
st.pyplot(plt)

# Add a line chart to display the exchange rate for the selected year
plt.figure(figsize=(12,6))
df_year = df[df.index.year == selected_year]
plt.plot(df_year.index, df_year['USD'], label='USD')
plt.plot(df_year.index, df_year['EUR'], label='EUR')
plt.plot(df_year.index, df_year['AUD'], label='AUD')
plt.xlabel("Date")
plt.ylabel("Exchange Rate") 
plt.title(f"Exchange Rate Trends for {selected_year}")
plt.legend()
st.pyplot(plt)