#!/usr/bin/env python
# coding: utf-8

# **Prediction of house prices**
# 
# Here I will try to analyse the features that impact house prices and build some models to predict the prices. I will use RMSE (root mean squared error) to measure the performance of the models.

# In[ ]:


# Lets importing some libraries 
import numpy as np # linear algebra
import matplotlib.pyplot as plt # for plotting 
import pandas as pd # for manipulating datasets
import seaborn as sb
from pylab import rcParams
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import scale
from collections import Counter


# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
rcParams['figure.figsize'] = 5, 4
sb.set_style('whitegrid')


# In[ ]:


# Laod the dataset
df = pd.read_csv('../input/kc_house_data.csv')


# In[ ]:


df.head()


# In[ ]:


# Lets see the some important stats
df.describe()


# In[ ]:


df.info()


# **Data Exploration**

# In[ ]:


#df correlation matrix shows relations between all variables in the dataset  
f,ax = plt.subplots(figsize=(17, 14))
sb.heatmap(df.corr(), annot=True,annot_kws={'size': 12}, linewidths=.5, fmt='.2f', ax=ax)


# As shown in the correlation matrix, mainly four variables have strong impact on the price 

# In[ ]:


# Lets select the main variable (important features) and review the insigts by using pairplots 
sb.set()
cols = df[['price','sqft_living','grade','sqft_above','bathrooms','sqft_living15']]
sb.pairplot(cols, size = 2.5)


# In[ ]:


# Correlation matrix between the target value (price) and important predictors.
k = 10 #number of variables for heatmap
corrmat = df.corr()
cols = corrmat.nlargest(k, 'price')['price'].index
cm = np.corrcoef(df[cols].values.T)
sb.set(font_scale=1.25)
f,ax = plt.subplots(figsize=(17, 14))
hm = sb.heatmap(cm, cbar=True, annot=True, square=True, fmt='.2f', ax=ax, annot_kws={'size': 12}, linewidths=.7, yticklabels=cols.values, xticklabels=cols.values)


# In[ ]:


#scatter plot 'sqft_living'/'price'
var = 'sqft_living'
data = pd.concat([df['price'], df[var]], axis=1)
data.plot.scatter(x=var, y='price', ylim=(0,8000000));
# there is a strong relationship between 'sqft_living' and 'price'


# In[ ]:


#boxplot 'grade'/'price'
var1 = 'grade'
data = pd.concat([df['price'], df[var1]], axis=1)
f, ax = plt.subplots(figsize=(8, 6))
fig = sb.boxplot(x=var1, y="price", data=data)
fig.axis(ymin=0, ymax=8000000);


# In[ ]:


#scatter plot 'sqft_living15'/'price'
var2 = 'sqft_living15'
data = pd.concat([df['price'], df[var2]], axis=1)
data.plot.scatter(x=var2, y='price', ylim=(0,8000000));
# There is a positive relationship between 'sqft_living15' and 'price' but not as well as 'sqft_living' 


# In[ ]:


#scatter plot 'sqft_above'/'price'
var3 = 'sqft_above'
data = pd.concat([df['price'], df[var3]], axis=1)
data.plot.scatter(x=var3, y='price', ylim=(0,8000000));


# In[ ]:


var4 = 'bathrooms'
data = pd.concat([df['price'], df[var4]], axis=1)
data.plot.scatter(x=var4, y='price', ylim=(0,8000000));


# In[ ]:


var5 = 'view'
data = pd.concat([df['price'], df[var5]], axis=1)
f, ax = plt.subplots(figsize=(8, 6))
fig = sb.boxplot(x=var5, y="price", data=data)
fig.axis(ymin=0, ymax=8000000)


# In[ ]:


# ratios
corrmat['price'].sort_values(ascending = False)


# In[ ]:


X = df[[var,var1,var2,var3,var4,var5,'sqft_basement','bedrooms','lat','waterfront','floors','yr_renovated']]
y = df['price']


# Sptlitting the dataset into test and training set. We will train our models in the training set and predict in test set

# In[ ]:


from sklearn.model_selection import train_test_split,cross_val_score, cross_val_predict
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2 , random_state = 1)


# In[ ]:


# Standardizing makes our data distributed normal and it is very usefull for a good prediction
from sklearn.preprocessing import StandardScaler

Scaler = StandardScaler()
X_train = Scaler.fit_transform(X_train)


# In[ ]:


# Fitting Multiple Linear Regression to the Training set
LinReg = LinearRegression()
LinReg.fit(X_train,y_train)
y_predict = LinReg.predict(X_test)

LinReg.score(X_train,y_train) # R squared 


# In[ ]:


def display_scores(scores):
    print(("Scores:", scores))
    print(("Mean:", scores.mean()))
    print(("Standard deviation:", scores.std()))


# By using cross_val_score we define some subsets (10 subsets here) and evaluate our model in these sets till finding a good estimator.
# 

# In[ ]:


lin_scores = cross_val_score(LinReg, X_train, y_train,
                             scoring="neg_mean_squared_error", cv=10)
lin_rmse_scores = np.sqrt(-lin_scores)
display_scores(lin_rmse_scores)


# In[ ]:


from sklearn.metrics import mean_squared_error

housing_predictions = LinReg.predict(X_train)
lin_mse = mean_squared_error(y_train, housing_predictions)
lin_rmse = np.sqrt(lin_mse)
lin_rmse


# In[ ]:


from sklearn.tree import DecisionTreeRegressor

tree_reg = DecisionTreeRegressor(random_state=42)
tree_reg.fit(X_train, y_train)


# In[ ]:


tree_scores = cross_val_score(tree_reg, X_train, y_train,
                             scoring="neg_mean_squared_error", cv=10)
tree_rmse_scores = np.sqrt(-tree_scores)
display_scores(tree_rmse_scores)


# In[ ]:


price_predictions = tree_reg.predict(X_train)
tree_mse = mean_squared_error(y_train, housing_predictions)
tree_rmse = np.sqrt(tree_mse)
tree_rmse


# In[ ]:


from sklearn.ensemble import RandomForestRegressor

forest_reg = RandomForestRegressor(random_state=42)
forest_reg.fit(X_train, y_train)


# In[ ]:


housing_predictions = forest_reg.predict(X_train)
forest_mse = mean_squared_error(y_train, housing_predictions)
forest_rmse = np.sqrt(forest_mse)
forest_rmse


# In[ ]:


forest_scores = cross_val_score(forest_reg, X_train, y_train,
                             scoring="neg_mean_squared_error", cv=10)
tree_rmse_scores = np.sqrt(-forest_scores)
display_scores(tree_rmse_scores)


# It seems that Random Forest regression makes better predictions than others so we select Random Forest for our model. Lets see the results in a new data (in the test set) 

# In[ ]:


from sklearn.model_selection import GridSearchCV

param_grid = [
    # try 12 (3×4) combinations of hyperparameters
    {'n_estimators': [3, 10, 30], 'max_features': [2, 4, 6, 8]},
    # then try 6 (2×3) combinations with bootstrap set as False
    {'bootstrap': [False], 'n_estimators': [3, 10], 'max_features': [2, 3, 4]},
  ]

forest_reg = RandomForestRegressor(random_state=42)
# train across 5 folds, that's a total of (12+6)*5=90 rounds of training 
grid_search = GridSearchCV(forest_reg, param_grid, cv=5,
                           scoring='neg_mean_squared_error')
grid_search.fit(X_train, y_train)


# In[ ]:


grid_search.best_params_


# In[ ]:


grid_search.best_estimator_


# In[ ]:


cvres = grid_search.cv_results_
for mean_score, params in zip(cvres["mean_test_score"], cvres["params"]):
    print((np.sqrt(-mean_score), params))


# In[ ]:


#154125.671031 result is the lowest RMSE, so we take 'max_features': 8 and n_estimators': 30.


# In[ ]:


feature_importances = grid_search.best_estimator_.feature_importances_
sorted(zip(feature_importances, X), reverse=True)


# In[ ]:


final_model = grid_search.best_estimator_

X_test_prepared = Scaler.fit_transform(X_test)
final_predictions = final_model.predict(X_test_prepared)

final_mse = mean_squared_error(y_test, final_predictions)
final_rmse = np.sqrt(final_mse)


# In[ ]:


final_rmse

