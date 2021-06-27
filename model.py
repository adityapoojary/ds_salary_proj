# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 18:00:11 2021

@author: adity
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('edu_data.csv')

# choose relevant columns

df_model = df[['Rating','Size','Type of ownership', 'Industry', 'Sector', 'Revenue',
        'avg_salary','hourly','employer_provided','num_comp','job_state', 'same_state', 'age', 'python_yn',
       'SparkR_yn', 'aws_yn', 'Excel_yn','seniority','desc_len','job_simp']]

# get dummy variables
df_dum = pd.get_dummies(df_model)

# train test split
from sklearn.model_selection import train_test_split
X = df_dum.drop('avg_salary',axis=1)
y = df_dum.avg_salary.values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Multiple Linear Regression
import statsmodels.api as sm

X_sm = sm.add_constant(X)
model = sm.OLS(y,X_sm).fit()
print(model.summary())

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

lm = LinearRegression()
lm.fit(X_train,y_train)

cross_val_score(lm,X_train,y_train,scoring='neg_mean_absolute_error',cv=3)

# Lasso Regression
# Random Forrest
# tune models GridSearchCV
# test ensembles



