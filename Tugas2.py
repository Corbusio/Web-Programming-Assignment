import streamlit as st
import pandas as pd

st.title("Tugas 2")

with st.sidebar:
	st.header("about Tugas 2")
	st.write("Widget = input text, radio button, button, slider")
	st.write("chart = line chart")
	st.write("layout = side bar, tab")
	st.write("database = google sheets")

tab1, tab2, tab3 = st.tabs(["Line Chart", "Widget", "DataBase"])
with tab1:
	df = pd.DataFrame({'column 1': [1,5,6,7,2], 'column 2': [2,7,6,5,1]})
	
	st.header("Line Chart")
	
	Chart_Data = df
	st.table(Chart_Data)
	st.line_chart(Chart_Data)

with tab2:
	st.header("Widget")
	nama = st.text_input('Nama','')
	jenis_kelamin = st.radio('Jenis Kelamin',('Pria','Wanita'))
	umur = st.slider('Umur :',0,100)
	
	if st.button('input'):
		st.subheader('Data diri')
		st.write('Nama = ',nama,
			'  \nJenis Kelamin = ',jenis_kelamin,
			'  \nUmur = ', umur)

with tab3:
	
	@st.cache_data(ttl=600)
	def load_data(sheets_url):
		#export file as csv
		csv_url = sheets_url.replace("/edit#gid=","/export?format=csv&gid=")
		return pd.read_csv(csv_url)

	df = load_data(st.secrets["public_gsheets_url"])

	for row in df.itertuples():
		st.write(f"{row.name} has a :{row.pet}:")
