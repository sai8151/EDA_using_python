import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#to ignore warnings
import warnings
warnings.filterwarnings('ignore')

population_data = pd.read_csv('global_air_pollution_data.csv')
pollution_data = pd.read_csv('world_population.csv')

# Inspect population data
print(population_data.head())
print(population_data.info())
print(population_data.describe())

# Inspect pollution data
print(pollution_data.head())
print(pollution_data.info())
print(pollution_data.describe())
