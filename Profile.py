import streamlit as st 
import pandas as pd
from streamlit_option_menu import option_menu
import pickle

data = pd.read_csv("updated_data.csv")

def run_website():
    with st.sidebar:
        selected = option_menu('Company Profile',
                            
                            ['Analytics Dashboard',
                             'Categorical ranking',
                            'Predicting success probability',
                             'Company Profile',
                            'Implement own dataset'],
                            default_index=0)
        
        
    if(selected == 'Company Profile'):

        st.write("To be coded")

        

run_website()
