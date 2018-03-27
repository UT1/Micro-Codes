# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 17:02:49 2018

@author: srivastavau
"""


import pandas as pd
import os
import seaborn as sns
import missingno as msno
import matplotlib.pyplot as plt


data_read = pd.read_csv('Data.csv', chunksize = 1000, encoding = "ISO-8859-1")

data = pd.concat(data_read,ignore_index=True)


#Check for the inconsistency of data using pyplot
df_missing = data.copy()
df_missing = df_missing.T
true = df_missing.isnull().sum(axis=1)
false = (len(df_missing.columns) - true)
df_missing['Valid Count'] = false / len(df_missing.columns)
df_missing['NA Count'] = true / len(df_missing.columns)

df_missing[['NA Count','Valid Count']].sort_values(
    'NA Count', ascending=True).plot.barh(
    stacked=True,figsize=(12,10), color=['c','y'])
plt.legend(loc=9)
plt.ylim(-1,24)
plt.title('Normed Missing Values Count', fontsize=20)
plt.xlabel('Normed (%) count', fontsize=20)
plt.ylabel('Column name', fontsize=20)
plt.show()



#Check for the inconsistency of data using missingno library
msno.matrix(data.sample(500))#matrix representation.. missing values left as blank
msno.bar(data.sample(1000))#bar sample of data
msno.heatmap(data)#Heatmap dependancy 
msno.dendrogram(data)