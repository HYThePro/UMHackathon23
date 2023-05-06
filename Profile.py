import streamlit as st 
import pandas as pd
from streamlit_option_menu import option_menu
import pickle

data = pd.read_csv("updated_data.csv")

def run_website():
    with st.sidebar:
        selected = option_menu('Venture Capital Analysis Website',
                            
                            ['Analytics Dashboard',
                             'Categorical ranking',
                            'Predicting success probability',
                             'Company Profile',
                            'Implement own dataset'],
                            default_index=0)
        
        
    if(selected == 'Company Profile'):

        input = st.selectbox(label='Name of company', options=data['name_c'])
        count = 0
        for value in data['name_c']:
            if input == values:
                st.write("Name of company: " , value)
                st.write("Incorporated date: ", data['count']['incorporated_date_c']
                count += 1

run_website()


