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
            if input == value:
                row = data.iloc[count]
                st.write("Incorporated date: ", row[1])
                st.write("Last valuation: ", row[3])
                st.write("Amount raised during last funding round: ", row[4])
                st.write("Date of last fund raise: ", row[6])
                st.write("Date of financial year end: ", row[7])
                st.write("Number of founder: ", row[12])
                st.write("Number of funding round: ", row[13])
                st.write("Number of shareholder: ", row[14])
                st.write("Minimum share in %: ", row[15])
                st.write("Median share in %: ", row[16])
                st.write("Maximum share in %: ", row[17])
                st.write("Categories: {}, {}, {}, {}, {}, {}, {}, {}".format(row[18], row[19], row[20], row[21], row[23], row[24], row[25], row[26]))
                chart_data = pd.DataFrame([[row[2], row[5], row[8], row[9], row[10], row[11]]], columns=["Total Funding", "Revenue", "Revenue growth", "EBIT", "Employee Growth (6m)", "Employee Growth (12m)"])
                st.bar_chart(chart_data)
            count = count+1
            

run_website()


