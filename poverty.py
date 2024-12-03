
#Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Create a sample dataset (in reality, you would use real data from sources like World Bank)
data = {
    'Country': ['USA', 'China', 'India', 'Brazil', 'South Africa'],
    'Poverty Rate (%)': [12.9, 17.2, 21.9, 18.7, 25.5],
    'GDP per Capita ($)': [69495, 10314, 2172, 9945, 6549],
    'Life Expectancy (years)': [78.7, 77.3, 69.5, 75.5, 64.1],
    'Human Development Index (HDI)': [0.924, 0.761, 0.645, 0.759, 0.699]
}

#Create a Pandas DataFrame
df = pd.DataFrame(data)

#Calculate the correlation matrix
corr_matrix = df[['Poverty Rate (%)', 'GDP per Capita ($)', 'Life Expectancy (years)', 'Human Development Index (HDI)']].corr()

#Print the correlation matrix
print(corr_matrix)

#Plot the correlation between poverty rate and GDP per capita
plt.figure(figsize=(8, 6))
plt.scatter(df['GDP per Capita ($)'], df['Poverty Rate (%)'])
plt.xlabel('GDP per Capita ($)')
plt.ylabel('Poverty Rate (%)')
plt.title('Correlation between Poverty Rate and GDP per Capita')
plt.show()

#plt.figure(figsize=(8, 6))
plt.scatter(df['Life Expectancy (years)'], df['Poverty Rate (%)'])
plt.xlabel('Life Expectancy (years)')
plt.ylabel('Poverty Rate (%)')
plt.title('Correlation between Poverty Rate and Life Expectancy')
plt.show()

#Plot the correlation between poverty rate and human development index
plt.figure(figsize=(8, 6))
plt.scatter(df['Human Development Index (HDI)'], df['Poverty Rate (%)'])
plt.xlabel('Human Development Index (HDI)')
plt.ylabel('Poverty Rate (%)')
plt.title('Correlation between Poverty Rate and Human Development Index')
plt.show()

