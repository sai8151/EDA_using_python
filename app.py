import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

#to ignore warnings
import warnings
warnings.filterwarnings('ignore')


population_data = pd.read_csv('world_population.csv')
pollution_data = pd.read_csv('global_air_pollution_data.csv')
print(pollution_data.columns)

# Display original column names
print("Original column names:")
print(population_data.columns)

# Display cleaned column names to verify
print("\nCleaned column names:")
print(population_data.columns)

print("\nGrowth Rate Column:")
print(population_data['Growth_Rate'].head(), population_data['Country'].head())


merged_data = pd.merge(pollution_data, population_data, on='Country', how='inner')

print("\nMerged Data:")
print(merged_data.head())


country = st.selectbox('Select a country:', merged_data['Country'].unique())
country_data = merged_data[merged_data['Country'] == country]

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=country_data, x='Growth_Rate', y='aqi_value', ax=ax)
ax.set_title(f'Pollution vs Growth Rate for {country}')
ax.set_xlabel('Growth Rate')
ax.set_ylabel('AQI Value')

# Display plot and description
st.pyplot(fig)
st.write(f"**Description for {country}:**")
st.write(f"The scatter plot above shows the relationship between the growth rate and AQI values for {country}.")