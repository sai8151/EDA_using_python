import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import time

# To ignore warnings
import warnings
warnings.filterwarnings('ignore')
with st.spinner(text="processing"):    
    # Load datasets
    population_data = pd.read_csv('world_population.csv')
    pollution_data = pd.read_csv('global_air_pollution_data.csv')
    
    # Clean column names
    pollution_data.columns = pollution_data.columns.str.strip().str.replace('\t', '').str.replace(' ', '_')
    population_data.columns = population_data.columns.str.strip().str.replace('\t', '').str.replace(' ', '_')
    
    # Rename columns to match
    pollution_data.rename(columns={'country_name': 'Country'}, inplace=True)
    population_data.rename(columns={'Country/Territory': 'Country'}, inplace=True)
    
    # Merge datasets
    merged_data = pd.merge(pollution_data, population_data, on='Country', how='inner')
    
    # Streamlit app
    st.title('Country Pollution and Population Analysis')
    
    # Select a country
    country = st.selectbox('Select a country:', merged_data['Country'].unique())
    country_data = merged_data[merged_data['Country'] == country]
    
    # Check if country_data is empty
    if country_data.empty:
        st.write("No data available for the selected country.")
    else:
        # Melt DataFrame for plotting
        melted_data = country_data.melt(id_vars=['Country', 'aqi_value'], 
                                        value_vars=['p2022', 'p2020', 'p2015', 'p2010', 'p2000', 'p1990', 'p1980', 'p1970'],
                                        var_name='Year', value_name='Population')
        
        # Ensure that AQI values are repeated correctly across years
        melted_data['aqi_value'] = country_data['aqi_value'].repeat(len(melted_data['Year'].unique())).values
        st.line_chart(data=melted_data,  x='Population', y='aqi_value', use_container_width=True)
        # Scatter Plot
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.scatterplot(data=melted_data, x='Population', y='aqi_value', hue='Year', ax=ax)
        ax.set_title(f'Pollution vs Population for India')
        ax.set_xlabel('Population')
        ax.set_ylabel('AQI Value')
        st.pyplot(fig)
    
    
        # Hexbin Plot
        fig1, ax1 = plt.subplots(figsize=(12, 6))
        hb = ax1.hexbin(melted_data['Population'], melted_data['aqi_value'], gridsize=30, cmap='viridis')
        cb = fig1.colorbar(hb, ax=ax1)
        ax1.set_title(f'Hexbin Plot: Pollution vs Population for {country}')
        ax1.set_xlabel('Population')
        ax1.set_ylabel('AQI Value')
        cb.set_label('Density')
        st.pyplot(fig1)
        st.write(f"**Hexbin Plot Description for {country}:**")
        st.write(f"The hexbin plot shows the density of data points with respect to the population and AQI values for {country}. The color intensity represents the concentration of data points.")
    
        # Joint Plot
        fig2 = plt.figure(figsize=(12, 6))
        joint_plot = sns.jointplot(data=melted_data, x='Population', y='aqi_value', kind='hex', cmap='viridis')
        joint_plot.fig.suptitle(f'Joint Plot: Pollution vs Population for {country}', y=1.02)
        st.pyplot(joint_plot.fig)
        st.write(f"**Joint Plot Description for {country}:**")
        st.write(f"The joint plot combines a scatter plot with a hexbin plot and histograms, illustrating the relationship between population and AQI values for {country}.")
    
        # 2D Density Plot
        fig3, ax3 = plt.subplots(figsize=(12, 8))
        sns.kdeplot(data=melted_data, x='Population', y='aqi_value', cmap='viridis', fill=True, ax=ax3)
        ax3.set_title(f'2D Density Plot: Pollution vs Population for {country}')
        ax3.set_xlabel('Population')
        ax3.set_ylabel('AQI Value')
        st.pyplot(fig3)
        st.write(f"**2D Density Plot Description for {country}:**")
        st.write(f"The 2D density plot displays the relationship between population and AQI values, with color gradients showing the density of data points for {country}.")
st.success('Done!') 
#st.balloons()
#st.snow()