import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.title("Tugas 3")

st.header('1. Write and Magic')
st.subheader("Write")
code = 'st.write("this is write")'
st.code(code, language='python')
st.subheader("result :")
st.write("this is write")

st.subheader("Magic")
code = '''Magic="Magic!!!:magic_wand:"
Magic'''
st.code(code, language='python')
Magic="Magic!!!:magic_wand:"
st.subheader("result :")
Magic

st.header('2. Text Elements')
st.subheader("st.code")
code = """ code = '''Magic='Magic!!!:magic_wand:'
Magic'''
st.code(code, language='python') """
st.code(code, language='python')
st.subheader("result :")
code = '''Magic="Magic!!!:magic_wand:"
Magic'''
st.code(code, language='python')

st.header('3. Data Display Elements')
st.subheader("st.Metric")
code = '''col1, col2, col3 = st.columns(3)
col1.metric("Fat", "10 kg", "+10%")
col2.metric("Muscle", "20 kg", "-5%")
col3.metric("Height", "175 cm", "+100cm")'''
st.code(code, language='python')

st.subheader("result :")
col1, col2, col3 = st.columns(3)
col1.metric("Fat", "10 kg", "+10%")
col2.metric("Muscle", "20 kg", "-5%")
col3.metric("Height", "175 cm", "+100cm")

st.header('4. Chart Elements')
st.subheader("st.bar_chart")
code = '''chart_data = pd.DataFrame(
	np.random.randn(20,3),
	columns=["a", "b", "c"])
st.bar_chart(chart_data)'''
st.code(code,language='python')
st.subheader("result :")
chart_data = pd.DataFrame(
	np.random.randn(20,3),
	columns=["a", "b", "c"])

st.bar_chart(chart_data)

st.header('5. Input Widgets')
st.subheader("st.color_picker")
code = '''color = st.color_picker('Warna', '#000000')
st.write('Warna terpilih = ', color)'''
st.code(code,language='python')
warna = st.color_picker('Warna', '#000000')
st.write('Warna terpilih = ', warna)

st.header('6. Media Elements')
st.subheader('st.image')
code = '''image = Image.open("GoodMorning.jpg")
st.image(image, caption="good morning")'''
st.code(code,language='python')
st.subheader('Result : ')
image = Image.open("GoodMorning.jpg")
st.image(image, caption="good morning")

st.header('7. Layouts and containers')
st.subheader('st.expander')
code = '''with st.expander("HIIIIIII"):
	Hi= Image.open("Hi.jpg")
	st.image(Hi, caption="HIIIIIIIII")'''
st.code(code,language='python')
st.subheader('Result : ')
with st.expander("HIIIIIII"):
	Hi= Image.open("Hi.jpg")
	st.image(Hi, caption="HIIIIIIIII")

st.header('8. Status Elements')
st.subheader('st.Error')
code = '''st.error('Error', icon="⚠️")'''
st.code(code,language='python')
st.subheader('Result : ')
st.error('Error', icon="⚠️")

st.header('9. Control flow')
st.subheader('st.Stop')
code = '''nama = st.text_input("Nama")
if not nama:
	st.warning("Masukan nama.")
	st.stop()
st.success("Terimakasih atas inputnya.")'''
st.code(code,language='python')
st.subheader('Result : ')
nama = st.text_input("Nama")
if not nama:
	st.warning("Masukan nama.")
	st.stop()
st.success("Terimakasih atas inputnya.")

st.header('10. Utilities')
st.subheader('st.help')
code='''st.help(st.line_chart)'''
st.code(code,language='python')
st.subheader('Result : ')
st.help(st.line_chart)