import streamlit as st
import pandas as pd

st.title("Yoyo matchs app")

input_name = st.text_input('Ton compte insta avec le @', '@yoyo_bdt')

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))
