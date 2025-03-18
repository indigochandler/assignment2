import pandas as pd 
import numpy as np  
import time  
import gc  
import psutil  
import os

sample_data = pd.read_csv("P2data1035.csv")
sample_data.head(10) 

data = pd.read_csv("P2data1035.csv", delimiter="\t")
data.head(10) 

print("Rows with missing values for 'T4' and 'T3':")
print(data[data[['T3', 'T4']].isna().all(axis=1)]) 
data = data.dropna(subset=['T3', 'T4'], how='all') 

data['T3'] = data['T3'].fillna(data.groupby('Level')['T3'].transform('mean')).round(1)
data['T4'] = data['T4'].fillna(data.groupby('Level')['T4'].transform('mean')).round(1)
data[['T3', 'T4']].isnull().sum()

descriptive_statistics = {}
for column in ['Level', 'T4', 'T3', 'T3adjusted', 'T4adjusted']:
    descriptive_statistics[column] = {
        "count": data[column].count(),
        "mean": data[column].mean(),
        "std": data[column].std(),
        "min": data[column].min(),
        "25%": data[column].quantile(.25),
        "50%": data[column].median(),
        "75%": data[column].quantile(.75),
        "max": data[column].max(),
    }
stats_table = pd.DataFrame(descriptive_statistics).round(2)
print("Descriptive Statistics Table:")
print(stats_table)
print()
print("Descriptive Statistics Using .describe():")
print()
print(data[['Level', 'T4', 'T3', 'T3adjusted', 'T4adjusted']].describe().round(2))

duplicates = data[data.duplicated()]
if len(duplicates) > 0:
    print(f"Number of repeated rows: {len(duplicates)}")
    print("Repeated rows:")
    duplicates = data[data.duplicated(keep=False)]
    print(duplicates)
else:
    print("No repeated rows found.")

