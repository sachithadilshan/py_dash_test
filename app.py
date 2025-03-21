import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="CBS Test Dashboard",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded")


with st.sidebar:
    st.title('🏂 CBS Dashboard')
    
    year_list = list(['2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020'])
    
    selected_year = st.selectbox('Select a year', year_list)

st.write("Hello world")



df = pd.DataFrame({
    "first column": [1, 2, 3, 4],
    "second column": [10, 20, 30, 40]
})

st.write(df)