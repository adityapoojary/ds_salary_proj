# Data Science Salary Estimator: Project Overview 
* Created a tool that estimates data science salaries (MAE ~ $ 11K) to help data scientists understand the average pay a professional can expect in this field.
* Engineered features from the text of each job description to quantify the value companies put on python, excel, aws, and spark. 
* Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model. 
* Built a client facing API using flask 

## Code and Resources Used 
**Python Version:** 3.7  
**Packages:** pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle  
**For Web Framework Requirements:**  ```pip install -r requirements.txt```  
**Flask Productionization:** https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2

**Data Collection:** https://github.com/PlayingNumbers/ds_salary_proj

## YouTube Project Walk-Through
https://www.youtube.com/playlist?list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t

## Data Cleaning
Data Colelcted needed to be cleaned so that it was usable for our model. The following changes were made:

*	Parsed numeric data out of salary 
*	Made columns for employer provided salary and hourly wages 
*	Removed rows without salary 
*	Parsed rating out of company text 
*	Made a new column for company state 
*	Added a column for if the job was at the company’s headquarters 
*	Transformed founded date into age of company 
*	Made columns for if different skills were listed in the job description:
    * Python  
    * R  
    * Excel  
    * AWS  
    * Spark 
*	Column for simplified job title and Seniority 
*	Column for description length 

## EDA
I looked at the distributions of the data and the value counts for the various categorical variables. Below are a few highlights:

![alt text](https://github.com/adityapoojary/ds_salary_proj/blob/master/position_salary.png "Salary by Position")

![alt text](https://github.com/adityapoojary/ds_salary_proj/blob/master/location.png "Job Opportunities by State")

![alt text](https://github.com/adityapoojary/ds_salary_proj/blob/master/correlation.png "Correlations")

![alt text](https://github.com/adityapoojary/ds_salary_proj/blob/master/industry.png "Job Opportunities by Industry")

## Model Building 

Transformation of the categorical variables into dummy variables was performed and split the data into train and tests sets with a test size of 20%.   

Three different models were built and evaluated using Mean Absolute Error. MAE was chosen because it is relatively easy to interpret and outliers aren’t particularly bad in for this type of model.   

I tried three different models:
*	**Multiple Linear Regression** – Baseline for the model
*	**Lasso Regression** – Because of the sparse data from the many categorical variables, I thought a normalized regression like lasso would be effective.
*	**Random Forest** – Again, with the sparsity associated with the data, I thought that this would be a good fit. 

## Model performance
The Random Forest model far outperformed the other approaches on the test and validation sets. 
*	**Random Forest** : MAE = 10.93
*	**Linear Regression**: MAE = 19.37
*	**Ridge Regression**: MAE = 20.08
