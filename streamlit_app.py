# Imports 

pip install openpyxl

import streamlit as st
import pandas as pd
import numpy as np

# Pandas options
pd.options.mode.chained_assignment = None
pd.set_option("display.max_columns", None)

# Streamlit
st.title("Yoyo matchs app")

input_name = st.text_input('Ton compte insta avec le @', '@yoyo_bdt')

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

# Python script
url = 'https://raw.githubusercontent.com/Guillem121198/machine_learning/main/players_22.csv'
players_22 = pd.read_csv(url, sep=',')

st.write(players_22)

match_table = pd.read_excel('yoyo_match_results.xlsx')
st.write(match_table)





