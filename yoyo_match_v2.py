# Imports 
import streamlit as st
import pandas as pd
import numpy as np

# Pandas options
pd.options.mode.chained_assignment = None
pd.set_option("display.max_columns", None)

# Streamlit UI/UX
st.title("yoyomatch 2.0 ❤️")

input_name = st.text_input('Ton compte insta en minuscules avec le @', '@')


# Reading csv file
url = 'extract_v3.csv'
matchs_df = pd.read_csv(url, sep=',')

# Renaming columns
matchs_df.columns = ['name', 'genre','genre_r','country','region','age','age_r','couple_type','couple_goal','life_type','life_type_r','first_date','song','couple_rythm','place','asset','asset_r','phone','mail','pay_date','amount']

# Cleaning spaces

matchs_df['name'] = matchs_df['name'].str.strip()
matchs_df['genre'] = matchs_df['genre'].str.strip()
matchs_df['genre_r'] = matchs_df['genre_r'].str.strip()
matchs_df['country'] = matchs_df['country'].str.strip()
matchs_df['region'] = matchs_df['region'].str.strip()
matchs_df['age'] = matchs_df['age'].str.strip()
matchs_df['age_r'] = matchs_df['age_r'].str.strip()
matchs_df['couple_type'] = matchs_df['couple_type'].str.strip()
matchs_df['couple_goal'] = matchs_df['couple_goal'].str.strip()
matchs_df['life_type'] = matchs_df['life_type'].str.strip()
matchs_df['life_type_r'] = matchs_df['life_type_r'].str.strip()
matchs_df['first_date'] = matchs_df['first_date'].str.strip()
matchs_df['song'] = matchs_df['song'].str.strip()
matchs_df['couple_rythm'] = matchs_df['couple_rythm'].str.strip()
matchs_df['place'] = matchs_df['place'].str.strip()
matchs_df['asset'] = matchs_df['asset'].str.strip()
matchs_df['asset_r'] = matchs_df['asset_r'].str.strip()
matchs_df['mail'] = matchs_df['mail'].str.strip()
matchs_df['pay_date'] = matchs_df['pay_date'].str.strip()

# Drop Yoyo & removing duplicates
matchs_df = matchs_df.drop([1])
matchs_df = matchs_df[-matchs_df.duplicated(subset=['name'], keep='last')]
matchs_df = matchs_df.reset_index(drop=True)

# Filling missing '@'
matchs_df['name_bis'] = ''
for i in range(len(matchs_df['name'])):
    if matchs_df['name'][i][0] != '@':
        matchs_df['name_bis'][i] = '@'
    else:
        matchs_df['name_bis'][i] = ''

matchs_df['name'] =  matchs_df['name_bis'] + matchs_df['name']
matchs_df['name'] = matchs_df['name'].str.lower()
matchs_df = matchs_df.drop(columns=['name_bis'])

# Rework some columns
matchs_df['asset_2'] = 'Unknown'
matchs_df['asset_2_r'] = 'Unknown'

matchs_df['asset_2'][matchs_df['asset'].str.contains('rire', na=False)] = 'Rire'
matchs_df['asset_2_r'][matchs_df['asset_r'].str.contains('rire', na=False)] = 'Rire'
matchs_df['asset_2'][matchs_df['asset'].str.contains('épaule', na=False)] = 'Epaule'
matchs_df['asset_2_r'][matchs_df['asset_r'].str.contains('épaule', na=False)] = 'Epaule'
matchs_df['asset_2'][matchs_df['asset'].str.contains('regard', na=False)] = 'Regard'
matchs_df['asset_2_r'][matchs_df['asset_r'].str.contains('regard', na=False)] = 'Regard'

# Testing compatibilities
try:
  input_data = matchs_df[matchs_df['name'] == input_name]

  new_matchs_df = matchs_df
  new_matchs_df['genre_matching'] = 0
  new_matchs_df['genre_matching'][matchs_df['genre'] == input_data.iloc[0]['genre_r']] = 1

  new_matchs_df['country_matching'] = 0
  new_matchs_df['country_matching'][matchs_df['country'] == input_data.iloc[0]['country']] = 1

  new_matchs_df['region_matching'] = 0
  new_matchs_df['region_matching'][matchs_df['region'] == input_data.iloc[0]['region']] = 1

  new_matchs_df['age_matching'] = 0
  new_matchs_df['age_matching'][matchs_df['age'] == input_data.iloc[0]['age_r']] = 1

  new_matchs_df['couple_type_matching'] = 0
  new_matchs_df['couple_type_matching'][matchs_df['couple_type'] == input_data.iloc[0]['couple_type']] = 1

  new_matchs_df['couple_goal_matching'] = 0
  new_matchs_df['couple_goal_matching'][matchs_df['couple_goal'] == input_data.iloc[0]['couple_goal']] = 1

  new_matchs_df['life_type_matching'] = 0
  new_matchs_df['life_type_matching'][matchs_df['life_type'] == input_data.iloc[0]['life_type_r']] = 1

  new_matchs_df['first_date_matching'] = 0
  new_matchs_df['first_date_matching'][matchs_df['first_date'] == input_data.iloc[0]['first_date']] = 1

  new_matchs_df['song_matching'] = 0
  new_matchs_df['song_matching'][matchs_df['song'] == input_data.iloc[0]['song']] = 1

  new_matchs_df['couple_rythm_matching'] = 0
  new_matchs_df['couple_rythm_matching'][matchs_df['couple_rythm'] == input_data.iloc[0]['couple_rythm']] = 1

  new_matchs_df['place_matching'] = 0
  new_matchs_df['place_matching'][matchs_df['place'] == input_data.iloc[0]['place']] = 1

  new_matchs_df['asset_matching'] = 0
  new_matchs_df['asset_matching'][matchs_df['asset_2'] == input_data.iloc[0]['asset_2_r']] = 1

  new_matchs_df['asset_matching_opp'] = 0
  new_matchs_df['asset_matching_opp'][matchs_df['asset_2_r'] == input_data.iloc[0]['asset_2']] = 1

  new_matchs_df['genre_matching_opp'] = 0
  new_matchs_df['genre_matching_opp'][matchs_df['genre_r'] == input_data.iloc[0]['genre']] = 1

  new_matchs_df['age_matching_opp'] = 0
  new_matchs_df['age_matching_opp'][matchs_df['age_r'] == input_data.iloc[0]['age']] = 1

  new_matchs_df['life_type_matching_opp'] = 0
  new_matchs_df['life_type_matching_opp'][matchs_df['life_type_r'] == input_data.iloc[0]['life_type']] = 1

  # Matching score computation
  new_matchs_df['matching_score'] = new_matchs_df['country_matching'] + new_matchs_df['region_matching'] + new_matchs_df['couple_type_matching'] + new_matchs_df['couple_goal_matching'] + new_matchs_df['life_type_matching']+ new_matchs_df['first_date_matching'] + new_matchs_df['song_matching'] + new_matchs_df['couple_rythm_matching'] + new_matchs_df['place_matching'] + new_matchs_df['asset_matching']+ new_matchs_df['asset_matching_opp']+ new_matchs_df['life_type_matching_opp']
  new_matchs_df['matching_score'] = round(((new_matchs_df['matching_score'] * 100/12) + 100)/200, 1)

  # Reworking final dataframe
  final_matching_df = new_matchs_df[(new_matchs_df['genre_matching'] == 1) & (new_matchs_df['genre_matching_opp'] == 1) & (new_matchs_df['age_matching_opp'] == 1) & (new_matchs_df['age_matching'] == 1)]
  final_matching_ui = final_matching_df.sort_values(by='matching_score', ascending=False).head(10)
  final_matching_ui['matching_score'] = final_matching_ui['matching_score'].map(str)
  final_matching_ui['matching_score'] = final_matching_ui['matching_score'] + "%"
  final_matching_v2 = final_matching_ui.rename(columns={"name": "Tes matchs", "matching_score": "Score d'affinité"})
  final_matching_v2.reset_index(inplace=True)
  final_matching_v2.index = final_matching_v2.index + 1

  # Displaying final dataframe
  st.write(final_matching_v2[["Tes matchs","Score d'affinité"]])
  
  st.markdown("C'est le moment de te jeter à l'eau ! Go slide dans les dm de tes matchs 😏")
  
except IndexError:
  st.error("Pseudo introuvable, n'oublie pas le '@' devant ton pseudo ni de le mettre tout en minuscules, si le problème persiste, merci de contacter @yoyobdt_")

