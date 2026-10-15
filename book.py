import streamlit as st
import requests 

st.set_page_config(page_title='Book Finder App',page_icon='📖')
st.title('Book Finder App 📖 ')
st.write('Discover The World Of Books')
book = st.text_input("Enter book name")

