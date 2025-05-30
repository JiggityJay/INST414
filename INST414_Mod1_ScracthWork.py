# INST414 Module 1: Maternal Mortality Rates
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Fetch data from the CDC dataset on Maternal Mortality
url = "https://data.cdc.gov/resource/e2d5-ggg7.json"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
else:
    print(f"Error: Unable to fetch data (Status Code: {response.status_code})")
    df = pd.DataFrame()  # Create an empty dataframe to prevent errors

# Ensure the dataset is not empty before proceeding
if not df.empty:
    # Display basic dataset info
    print("Dataset Overview:")
    print(df.head())  # First 5 rows
    print(df.info())  # Column names & data types
    print(df.describe())  # Summary stats for numerical columns
    print("Missing Values Per Column:\n", df.isnull().sum())  # Count missing values
    print("Duplicate Rows Count:", df.duplicated().sum())  # Check for duplicates

    # Check unique values per column
    print("\nUnique Values per Column:")
    for col in df.columns:
        print(f"{col}: {df[col].nunique()} unique values")

    # Replace "column_name" with an actual numerical column name
    numerical_column = "maternal_deaths"  # Update with the correct column name
    if numerical_column in df.columns:
        # Histogram of the selected numerical column
        plt.figure(figsize=(8, 5))
        sns.histplot(df[maternal_deaths], kde=True, bins=30)
        plt.title(f"Distribution of {maternal_deaths}")
        plt.xlabel(maternal_deaths)
        plt.ylabel("Frequency")
        plt.show()

        # Outlier Detection using IQR
        Q1 = df[maternal_deaths].quantile(0.25)
        Q3 = df[maternal_deaths].quantile(0.75)
        IQR = Q3 - Q1
        outliers = df[(df[maternal_deaths] < (Q1 - 1.5 * IQR)) | 
                      (df[maternal_deaths] > (Q3 + 1.5 * IQR))]
        print(f"\nOutliers in {maternal_deaths}:\n", outliers)
    else:
        print(f"Column '{maternal_deaths}' not found in the dataset.")

    # Convert categorical variables into dummy/indicator variables
    categorical_column = "group"  # Update with actual column name
    if categorical_column in df.columns:
        df = pd.get_dummies(df, columns=[group], drop_first=True)
        print("\nCategorical variables have been converted into dummy variables.")
    else:
        print(f"Column '{group}' not found for encoding.")

else:
    print("No data available to analyze.")
