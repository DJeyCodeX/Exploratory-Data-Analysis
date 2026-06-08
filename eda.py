# -*- coding: utf-8 -*-
"""EDA.ipynb"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#to ignore warnings
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv("/content/drive/MyDrive/Practice/used_cars_data.csv")

df.head()

df.isnull().sum()

df.info()

df['Mileage_unit'] = df['Mileage'].str.split().str.get(1)
df['Engine_unit'] = df['Engine'].str.split().str.get(1)
df['Power_unit'] = df['Power'].str.split(' ').str.get(1)

df.head()

df['Mileage'] = df['Mileage'].str.split().str.get(0).astype('float64')
df['Engine'] = df['Engine'].str.split().str.get(0).astype('float64')
df['Power'] = df['Power'].str.split().str.get(0)

print(df.to_markdown())

df.nunique()

"""#Data Reduction"""

df = df.drop(['S.No.'], axis = 1)

df.head()

"""##Creating Features"""

from datetime import date

df['Car_Age'] = date.today().year - df['Year']

df.head()

df['Brand'] = df.Name.str.split().str.get(0)

df['Model'] = df.Name.str.split().apply(lambda x: ' '.join(x[1:]))

df.head()

"""##Data Cleaning/Wrangling"""

print(df.Brand.unique())
print(df.Brand.nunique())

df["Brand"].replace({"ISUZU": "Isuzu", "Mini": "Mini Cooper","Land":"Land Rover"}, inplace=True)

"""##EDA Exploratory Data Analysis


*   EDA can be leveraged to check for outliers, patterns, and trends in the given data.
*   EDA helps to find meaningful patterns in data.
*   EDA provides in-depth insights into the data sets to solve our business problems.
*   EDA gives a clue to impute missing values in the dataset




"""

df.describe(include='all').T

df['New_Price_Unit'] = df['New_Price'].str.split().str.get(1)
df['New_Price'] = df['New_Price'].str.split().str.get(0).astype('float64')

df.head()

cat_cols=df.select_dtypes(include=['object']).columns
num_cols = df.select_dtypes(include=np.number).columns.tolist()
print("Categorical Variables:")
print(cat_cols)
print("Numerical Variables:")
print(num_cols)

new_df = df[['Name', 'Location','Brand', 'Model', 'Year', 'Kilometers_Driven', 'Fuel_Type', 'Transmission', 'Owner_Type', 'Mileage', 'Engine', 'Power', 'Seats', 'Price', 'Car_Age', 'New_Price']]

new_df.head()

new_df.describe(include='all').T

cat_cols=new_df.select_dtypes(include=['object']).columns
num_cols = new_df.select_dtypes(include=np.number).columns.tolist()
print("Categorical Variables:")
print(cat_cols)
print("Numerical Variables:")
print(num_cols)

"""##EDA Univariate Analysis"""

#For numerical columns

for col in num_cols:
    print(col)
    print('Skew :', round(new_df[col].skew(), 2))
    plt.figure(figsize = (15, 4))
    plt.subplot(1, 2, 1)
    new_df[col].hist(grid=False)
    plt.ylabel('count')
    plt.subplot(1, 2, 2)
    sns.boxplot(x=new_df[col])
    plt.show()

# for categorical columns

for col in cat_cols:
    print(col)
    # print('Skew :', round(new_df[col].skew(), 2))
    plt.figure(figsize =  (18, 18))
    plt.subplot(1, 2, 1)
    plt.suptitle(f'Bar plot for categorical Column {col} in the dataset')
    sns.countplot( x = col, data = new_df, color = 'blue',
              order = new_df[col].head(20).value_counts().index);
    plt.xticks(rotation=90)
    plt.show()

"""## Transformation"""

sns.distplot(new_df["Kilometers_Driven"], axlabel="Kilometers_Driven");

sns.distplot(new_df["Price"], axlabel="Price");

sns.distplot(new_df["New_Price"], axlabel="New_Price");

"""Normalization is useful for when a distribution is unknown or not normal (not bell curve), while standardization is useful for normal distributions."""

def log_transform(data,col):
    for colname in col:
        if (data[colname] == 1.0).all():
            data[colname + '_log'] = np.log(data[colname]+1)
        else:
            data[colname + '_log'] = np.log(data[colname])
    data.info()

log_transform(new_df,col=['Kilometers_Driven', 'Price'])

sns.distplot(new_df["Kilometers_Driven_log"], axlabel="Kilometers_Driven_log");

sns.distplot(new_df["Price_log"], axlabel="Price_log");

"""##Bivariate Analysis



*   For Numerical variables, Pair plots and Scatter plots are widely been used to do Bivariate Analysis.

*   A Stacked bar chart can be used for categorical variables if the output variable is a classifier. Bar plots can be used if the output variable is continuous


"""

#for numerical variables
plt.figure(figsize=(13,17))
sns.pairplot(data=new_df.drop(['Kilometers_Driven','Price'],axis=1))
plt.show()

#For Categorical Variables

fig, axarr = plt.subplots(4, 2, figsize=(12, 18))
new_df.groupby('Location')['Price_log'].mean().sort_values(ascending=False).plot.bar(ax=axarr[0][0], fontsize=12)
axarr[0][0].set_title("Location Vs Price", fontsize=18)
new_df.groupby('Transmission')['Price_log'].mean().sort_values(ascending=False).plot.bar(ax=axarr[0][1], fontsize=12)
axarr[0][1].set_title("Transmission Vs Price", fontsize=18)
new_df.groupby('Fuel_Type')['Price_log'].mean().sort_values(ascending=False).plot.bar(ax=axarr[1][0], fontsize=12)
axarr[1][0].set_title("Fuel_Type Vs Price", fontsize=18)
new_df.groupby('Owner_Type')['Price_log'].mean().sort_values(ascending=False).plot.bar(ax=axarr[1][1], fontsize=12)
axarr[1][1].set_title("Owner_Type Vs Price", fontsize=18)
new_df.groupby('Brand')['Price_log'].mean().sort_values(ascending=False).head(10).plot.bar(ax=axarr[2][0], fontsize=12)
axarr[2][0].set_title("Brand Vs Price", fontsize=18)
new_df.groupby('Model')['Price_log'].mean().sort_values(ascending=False).head(10).plot.bar(ax=axarr[2][1], fontsize=12)
axarr[2][1].set_title("Model Vs Price", fontsize=18)
new_df.groupby('Seats')['Price_log'].mean().sort_values(ascending=False).plot.bar(ax=axarr[3][0], fontsize=12)
axarr[3][0].set_title("Seats Vs Price", fontsize=18)
new_df.groupby('Car_Age')['Price_log'].mean().sort_values(ascending=False).plot.bar(ax=axarr[3][1], fontsize=12)
axarr[3][1].set_title("Car_Age Vs Price", fontsize=18)
plt.subplots_adjust(hspace=1.0)
plt.subplots_adjust(wspace=.5)
sns.despine()

"""##Multivariate Analysis

A heat map is widely been used for Multivariate Analysis

Heat Map gives the correlation between the variables, whether it has a positive or negative correlation.
"""

num_cols

new_df[['Year',
 'Kilometers_Driven',
 'Mileage',
 'Engine',
 'Seats',
 'Price',
 'Car_Age',
 'New_Price']]

plt.figure(figsize=(12, 7))
sns.heatmap(new_df[['Year',
 'Kilometers_Driven',
 'Mileage',
 'Engine',
 'Seats',
 'Price',
 'Car_Age',
 'New_Price']].corr(), annot = True, vmin = -1, vmax = 1)
plt.show()

