from turtle import color
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data. Set index to the 'date' column. 
df = pd.read_csv('fcc-forum-pageviews.csv', index_col=['date'])

# Clean data by filtering out page views 
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]
df.index = pd.to_datetime(df.index)

# Draw a line plot 
def draw_line_plot():
    fig, ax = plt.subplots(figsize=(16,9))
    ax= sns.lineplot(data=df, x=df.index, y=df['value'], color='firebrick')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    return fig

# Draw a Bar Plot  
def draw_bar_plot():
    """ Copy and modify data for monthly bar plot """
    df_bar = df.copy()

# Group datatime by month and then into year
    df_bar= df_bar.groupby(pd.Grouper(freq='M')).mean().rename(columns={'value': 'daily avg'})
    df_bar['year'] = pd.DatetimeIndex(df_bar.index).year
    df_bar['month'] = pd.DatetimeIndex(df_bar.index).strftime('%B')

    """ Draw bar plot """
    fig, ax = plt.subplots(figsize=(16,9))
    ax = sns.barplot(x='year', y='daily avg', data=df_bar, hue='month', hue_order=['January', 'February', 'March','April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],palette='tab10' )
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    plt.legend(title='Months', loc='upper left')

    return fig

# Draw box plot
def draw_box_plot():

    """ Prepare date for box plots  """
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    fig, (ax1,ax2) = plt.subplots(1,2)
    ax1 = sns.boxplot(data = df_box, x='year', y='value', ax=ax1)
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax2 = sns.boxplot(data=df_box, x='month', y='value', ax=ax2, order=['Jan', 'Feb', 'Mar','Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')
    ax2.set_title('Month-wise Box Plot (Seasonality)')   

    return fig