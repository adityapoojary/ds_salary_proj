# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 23:33:06 2021

@author: adity
"""

import pandas as pd
import numpy as np

df = pd.read_csv('Uncleaned_DS_jobs.csv')

# AVG SALARY
df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)  


df = df[df['Salary Estimate']!='-1']
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minuskd = salary.apply(lambda x: x.replace('K','').replace('$',''))

min_hr = minuskd.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary:',''))

df['min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = min_hr.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary+df.max_salary)/2

# COMPANY TEXT ONLY
df['company_text'] = df.apply(lambda x: x['Company Name'] if x['Rating']<0 else x['Company Name'][:-3],axis=1)

# JOB STATE
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[-1])
print(df.job_state.value_counts())

df['same_state'] = df.apply(lambda x: 1 if x.Location==x.Headquarters else 0,axis = 1)

# AGE OF THE COMPANY
df['age'] = df.Founded.apply(lambda x: x if x<1 else 2020-x)

# Python 
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
print(df.python_yn.value_counts())

# R Studio
df['R_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' else 0)
print(df.R_yn.value_counts())


# Spark
df['SparkR_yn'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
print(df.SparkR_yn.value_counts())

# aws
df['aws_yn'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
print(df.SparkR_yn.value_counts())

#Excel
df['Excel_yn'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
print(df.Excel_yn.value_counts())

df_out = df.drop(['index'],axis = 1)
df.to_csv('salary_cleaned.csv',index = False)