import streamlit as st
import pandas as pd

st.title("Tugas 1")

st.header("Table")
Data = pd.DataFrame({"Tikus": [2,3,9,5,1], "Sapi": [7,2,9,5,6]})
st.write(Data)

st.header("Line Chart")
st.line_chart(Data)