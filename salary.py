# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 18:28:40 2021

@author: adity
"""
import glassdoor_scrapper as gs
import pandas as pd

path = "C:/Users/adity/Documents/ds_salary_proj/chromedriver"

df = gs.get_jobs('data scientist',15,False,path,15)
