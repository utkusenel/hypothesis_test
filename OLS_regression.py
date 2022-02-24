#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 16:34:25 2022

@author: utkusenel
"""

import pandas as pd
import numpy as np
from sklearn import datasets, linear_model
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from scipy import stats
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder


df = pd.read_excel("/Users/utkusenel/Desktop/2. EL TOPLAM SATIŞ.xlsx", sheet_name = "Sheet1")
X = df[["Satış Tutarı", "Km", "Hasar"]]
y = df.Segment
min_max_scaler = preprocessing.MinMaxScaler()
X_minmax = min_max_scaler.fit_transform(X)

labelencoder = LabelEncoder()
df["Segment_N"] = labelencoder.fit_transform(y)

print(X_minmax)


X2 = sm.add_constant(X_minmax)
est = sm.OLS(df["Segment_N"], X2)
est2 = est.fit()
print(est2.summary())


means=[]

for columns in range(1,16):
    df_mean = df.iloc[:,columns].mean()
    means.append(df_mean)
    
    
print(means)
    
    
