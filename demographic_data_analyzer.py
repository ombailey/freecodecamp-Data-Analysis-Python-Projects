import pandas as pd
import numpy as np

df = pd.read_csv('adult.data.csv')

# How many people of each race are represented in this dataset?
x = []
x.append((sum(df['race'] == 'White')))
x.append((sum(df['race'] == 'Black')))
x.append((sum(df['race'] == 'Asian-Pac-Islander')))
x.append((sum(df['race'] == 'Amer-Indian-Eskimo')))
x.append((sum(df['race'] == 'Other')))

race_count = pd.Series(x, index=df['race'].unique())

# What is the average age of men?
males = df[df['sex'] == 'Male']
average_age_men= round(np.average(males['age']),1)

#What is the percentage of people who have a Bachelor's degree?
percentage_bachelors = round((sum(df['education'] == 'Bachelors') / len(df)) * 100, 1)

# What percentage people with advanced education (Bachelors, Masters, Or Doctorate) make more than 50k? em = dataframe that shows education and money
em = (df[['education', 'salary']])
em = em[em['salary'] == '>50K']
rich_advanced_education = (sum(em['education'] == 'Bachelors') + sum(em['education'] == 'Masters') + sum(em['education'] == 'Doctorate'))
adv_edu = sum(df['education'] == 'Bachelors') + sum(df['education'] == 'Masters') + sum(df['education'] == 'Doctorate')
higher_education_rich = round(rich_advanced_education / adv_edu * 100, 1)

# What percentage of people without advanced education make more than 50K?
rich_advanced_education = (sum(em['education'] == 'Bachelors') + sum(em['education'] == 'Masters') + sum(em['education'] == 'Doctorate'))
lower_education_rich = round(((len(em) - rich_advanced_education) / (len(df) - adv_edu) * 100),1)

# What is the minimum number of hours a person works per week?
min_work_hours = np.min(df['hours-per-week'])

# What percentage of people who work the minimum number of hours per week have a salary of more than 50K?
wm = (df[['hours-per-week', 'salary']])
wm = wm[wm['hours-per-week'] == np.min(df['hours-per-week'])]

num_min_workers = len(wm)
rich_percentage = ((sum(wm['salary'] == '>50K')) / len(wm)) * 100

# What country has the highest percentage of people that earn >50k and what is that percentage?
rich_country = df[['native-country', 'salary']]
rich_country = rich_country[rich_country['salary'] == '>50K']
rich_country_num = rich_country['native-country'].value_counts()

country_pop = df['native-country'].value_counts()
country_avg = rich_country_num / country_pop
highest_earning_country = country_avg.idxmax()
highest_earning_country_percentage = round(country_avg.loc['Iran'] * 100, 1)

#Identify the most popular occupation for those who earn >50k in India.
india = df[['native-country', 'salary', 'occupation']]
india = india[india['native-country'] == 'India']
india = india[india['salary'] == '>50K']
top_IN_occupation = india['occupation'].value_counts().idxmax()