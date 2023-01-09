import streamlit as st
import streamlit.components.v1 as components

# >>> import plotly.express as px
# >>> fig = px.box(range(10))
# >>> fig.write_html('https://github.com/12Shraddha/Portfolio/blob/master/home.html')

st.header("test html import")

HtmlFile = open("https://github.com/12Shraddha/Portfolio/blob/master/home.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
print(source_code)
components.html(source_code)
