from itertools import count, groupby
from unicodedata import name
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Importing Data
df =pd.read_csv('medical_examination.csv')

""" Adding Overweight column """
# Convert weight from cm to m
height_meter = (df['height'] / 100) ** 2

#Calculating BMI and creating overweight column
df['overweight'] = df['weight'] / height_meter

#Convert weight to 0 and 1. O if underweight(below 25) or 1 if overweight(above 25)
df['overweight'] = np.where(df['overweight'] >25, 1, 0)

#Convert data type from float to int
df['overweight'] = df['overweight'].astype(int)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = np.where(df['cholesterol'] == 1, 0, 1)
df['gluc'] = np.where(df['gluc'] == 1, 0, 1)

def draw_cat_plot():
# Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df,value_vars=['active', 'alco','cholesterol', 'gluc', 'overweight', 'smoke'], id_vars=['cardio'])
    vars_order = ['active', 'alco','cholesterol', 'gluc', 'overweight', 'smoke']
    df_cat = df_cat.value_counts().reset_index(name='total')

# Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    fig = sns.catplot(x='variable', y = 'total', hue= 'value', data=df_cat, col='cardio' , kind='bar', order=vars_order)
    fig.set_xlabels('variable')
    fig.set_ylabels('total')
    fig = fig.fig
    return fig

def draw_heat_map():
# Clean the data. Filter out the following patient segments thare incorrect.
    df_heat = df.loc[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]

# Calculate the correlation matrix
    corr = df_heat.corr()

# Generate a mask for the upper triangle
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True

# Set up the matplotlib figure
    fig, ax = plt.subplots(figsize = (12,9))

#Draw the heatmap
    ax = sns.heatmap(corr, mask=mask, square=True, vmax=.3, fmt='.1f', annot=True)
    return fig
