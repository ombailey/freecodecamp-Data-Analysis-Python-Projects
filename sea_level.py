import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress 

# Read data from file
df = pd.read_csv('epa-sea-level.csv')

# Create scatter plot
plt.scatter(data=df, x='Year', y='CSIRO Adjusted Sea Level', c='b')

# Create first line of best fit
""" Add Years up to 2050 for best fit line """
""" Plot the Line """
x= df['Year']
y= df['CSIRO Adjusted Sea Level']
result = linregress(x,y)
m = result.slope
b = result.intercept
years = range(1880,2051)
plt.plot(years, m * years + b, c='r', label='first best line')

# Create second line of best fit
new_df = df[df['Year'] >= 2000]
res = linregress(new_df['Year'],new_df['CSIRO Adjusted Sea Level'])
m = res.slope
b = res.intercept
years = range(2000,2051)
plt.plot(years, m * years + b, c = 'g', label='second best line')

#Add labels and title
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
plt.xticks([1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0])


