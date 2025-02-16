#INST414 Module 1: Maternal Mortality Rates
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://data.cdc.gov/resource/e2d5-ggg7.json" #is the link to the CDC dataset on Maternal Mortality 
response = requests.get(url) #
data = response.json()
df = pd.DataFrame(data)

df.head()  # First 5 rows
df.tail()  # Last 5 rows
df.shape   # (rows, columns)
df.info()  # Column names & data types
df.describe()  # Summary stats for numerical columns
df.isnull().sum()  # Count of missing values per column
df.duplicated().sum()  # Check for duplicate rows

for col in df.columns: #to check for unique values
    print(f"{col}: {df[col].nunique()} unique values") 

sns.histplot(df["group"], kde=True, bins=30) #creates a histogram of the collected data
plt.show()

#This section is still a work in progress
#Q1 = df["group"].quantile(0.25) #displays the data outliears in the 1st & 3rd Quartile
#Q3 = df["group"].quantile(0.75)
#IQR = Q3 - Q1
#outliers = df[(df["subgroup"] < (Q1 - 1.5 * IQR)) | (df["column_name"] > (Q3 + 1.5 * IQR))]
#print(outliers)

#df = pd.get_dummies(df, columns=["category_column"], drop_first=True) #helps convert any categorical data into quantitative data