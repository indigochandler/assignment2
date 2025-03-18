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


