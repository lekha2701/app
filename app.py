import streamlit as st
import joblib


model_nb = joblib.load('News-Category')

st.title('NEWS-CATEGORY CLASSIFIER')
ip = st.text_input('Enter the news')

op = model_nb.predict([ip])
if st.button('PREDICT')
st.title(op[0])
