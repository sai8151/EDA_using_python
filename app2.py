from pygwalker.api.streamlit import StreamlitRenderer
import pandas as pd
import streamlit as st
 
# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="Use Pygwalker In Streamlit",
    layout="wide"
)
 
# Add Title
st.title("Use Pygwalker In Streamlit")
 
import pygwalker as pyg

@st.cache_resource
def get_pyg_renderer() -> "StreamlitRenderer":
    population_data = pd.read_csv('world_population.csv')
    pollution_data = pd.read_csv('global_air_pollution_data.csv')

    pollution_data.columns = pollution_data.columns.str.strip().str.replace('\t', '').str.replace(' ', '_')
    population_data.columns = population_data.columns.str.strip().str.replace('\t', '').str.replace(' ', '_')



    # Rename columns to match
    #pollution_data.rename(columns={'country_name': 'Country'}, inplace=True)
    #population_data.rename(columns={'Country': 'Country'}, inplace=True)

    # Merge datasets
    merged_data = pd.merge(pollution_data, population_data, on='Country', how='inner')
    walker = pyg.walk(merged_data)
    return StreamlitRenderer(merged_data, spec="./gw_config.json", spec_io_mode="rw")

 
renderer = get_pyg_renderer()
 
renderer.explorer()