# Imports 

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
url = 'https://raw.githubusercontent.com/Guillem121198/matching_app/main/yoyo_match_results_v4.csv'
matchs_df = pd.read_csv(url, sep=',')

matchs_df.columns = ['name', 'genre','yeux','cheveux','physique','mental','important','genre_r','yeux_r','cheveux_r','physique_r','mental_r','important_r','age','age_r','nb_crit_ok','nb_matchs']

input_data = matchs_df[matchs_df['name'] == input_name]

new_matchs_df = matchs_df
new_matchs_df['genre_matching'] = 0
new_matchs_df['genre_matching'][matchs_df['genre'] == input_data.iloc[0]['genre_r']] = 1

new_matchs_df['yeux_matching'] = 0
new_matchs_df['yeux_matching'][matchs_df['yeux'] == input_data.iloc[0]['yeux_r']] = 1

new_matchs_df['cheveux_matching'] = 0
new_matchs_df['cheveux_matching'][matchs_df['cheveux'] == input_data.iloc[0]['cheveux_r']] = 1

new_matchs_df['physique_matching'] = 0
new_matchs_df['physique_matching'][matchs_df['physique'] == input_data.iloc[0]['physique_r']] = 1

new_matchs_df['mental_matching'] = 0
new_matchs_df['mental_matching'][matchs_df['mental'] == input_data.iloc[0]['mental_r']] = 1

new_matchs_df['important_matching'] = 0
new_matchs_df['important_matching'][matchs_df['important'] == input_data.iloc[0]['important_r']] = 1

new_matchs_df['age_matching'] = 0
new_matchs_df['age_matching'][matchs_df['age'] == input_data.iloc[0]['age_r']] = 1

new_matchs_df['genre_matching_opp'] = 0
new_matchs_df['genre_matching_opp'][matchs_df['genre_r'] == input_data.iloc[0]['genre']] = 1

new_matchs_df['yeux_matching_opp'] = 0
new_matchs_df['yeux_matching_opp'][matchs_df['yeux_r'] == input_data.iloc[0]['yeux']] = 1

new_matchs_df['cheveux_matching_opp'] = 0
new_matchs_df['cheveux_matching_opp'][matchs_df['cheveux_r'] == input_data.iloc[0]['cheveux']] = 1

new_matchs_df['physique_matching_opp'] = 0
new_matchs_df['physique_matching_opp'][matchs_df['physique_r'] == input_data.iloc[0]['physique']] = 1

new_matchs_df['mental_matching_opp'] = 0
new_matchs_df['mental_matching_opp'][matchs_df['mental_r'] == input_data.iloc[0]['mental']] = 1

new_matchs_df['important_matching_opp'] = 0
new_matchs_df['important_matching_opp'][matchs_df['important_r'] == input_data.iloc[0]['important']] = 1

new_matchs_df['age_matching_opp'] = 0
new_matchs_df['age_matching_opp'][matchs_df['age_r'] == input_data.iloc[0]['age']] = 1



new_matchs_df['matching_score'] = new_matchs_df['yeux_matching'] + new_matchs_df['cheveux_matching'] + new_matchs_df['physique_matching'] + new_matchs_df['mental_matching'] + new_matchs_df['important_matching']+ new_matchs_df['age_matching'] + new_matchs_df['yeux_matching_opp'] + new_matchs_df['cheveux_matching_opp'] + new_matchs_df['physique_matching_opp'] + new_matchs_df['mental_matching_opp']+ new_matchs_df['important_matching_opp']+ new_matchs_df['age_matching_opp']



final_matching_df = new_matchs_df[(new_matchs_df['genre_matching'] == 1) & (new_matchs_df['genre_matching_opp'] == 1)]

st.write(final_matching_df.sort_values(by='matching_score', ascending=False).head(5))





