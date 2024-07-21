import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
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

# Print the 'Growth Rate' column (now 'Growth_Rate' after cleaning)
print("\nGrowth Rate Column:")
print(population_data['Growth_Rate'].head(), population_data['Country'].head())
