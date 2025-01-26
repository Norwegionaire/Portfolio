# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 08:30:27 2024

@author: engeb
"""

import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import pandas as pd
from statsmodels.stats.multicomp import pairwise_tukeyhsd
# =============================================================================
# def regression_model():
#     x1 = int(input("x1 = "))
#     y1 = int(input("y1 = "))
#     x2 = int(input("x2 = "))
#     y2 = int(input("y2 = "))
#     
#     m = (y2 - y1)/(x2 - x1)
#     b = y1 - m * x1
#     return b
# 
# print(regression_model())
# =============================================================================


# =============================================================================
# def linear_model():
#      X = np.array([1, 20, 30, 40])
#      Y = np.array([1, 400, 800, 1300])
#      beta1, beta0 = np.polyfit(X, Y, 1)
#      print(beta1, beta0)
#      y_pred = beta0 + beta1 * X
#      #e = Y - y_pred
#      plt.plot(X,Y,"o", label = "Data Points")
#      plt.plot(X, y_pred, label = "Regression Line")
#      for i in range(len(X)):
#          plt.vlines(X[i], y_pred[i], Y[i], color = "red", linestyle = "--")
#      plt.legend()
#      plt.show()
# 
# linear_model()
# =============================================================================

# =============================================================================
# def stat_model():
#     data = pd.read_csv("Data_example2.csv", sep=";")
#     X = data["X"]
#     Y = data["Y"]
#     
#     x_with_const = sm.add_constant(X) #add a constant to the independent value
#     
#     model = sm.OLS(Y, x_with_const).fit() #fit the linear regression model
#     predictions = model.predict(x_with_const)
#     
#     #plotting
#     plt.figure(figsize=(10, 6))
#     plt.scatter(X, Y, label = "Data Points", color = "blue")
#     plt.plot(X, predictions, label = "Regression", color = "red")
#     plt.title("Regression Line Fit")
#     plt.xlabel("X")
#     plt.ylabel("Y")
#     plt.legend()
#     plt.grid()
#     plt.show()
# 
# =============================================================================
# =============================================================================
# def current_task():
#     cars = pd.read_table("vehicles.txt", sep="\t", header = 0, index_col = 0)
#     X = cars["horsepower"]
#     Y = cars["consumption"]
# 
#     beta1, beta0 = np.polyfit(X, Y, 1)
#     print(f"Beta1 is {beta1}, Beta0 is {beta0}")
#     y_predict = beta0 + beta1*X
#     
#     x_constant = sm.add_constant(X)
#     cars_model = sm.OLS(Y, x_constant).fit()
#     predictions = cars_model.predict(x_constant)
#     
#     plt.figure(figsize=(10, 6))
#     plt.scatter(X, Y, label = "Data Points", color="orange")
#     plt.plot(X, predictions, label = "Regression Line", color="blue")
#     for i in range(len(X)):
#         plt.vlines(X[i], y_predict[i], Y[i], color = "red", linestyle = "--")
#     plt.title("Horsepower to Consumption")
#     plt.xlabel("Horsepower")
#     plt.ylabel("Consumptions")
#     plt.legend()
#     plt.show()
# 
# current_task()
# 
# =============================================================================

# =============================================================================
# #data
# def summary():
#     X = np.array([1, 20, 30 ,40])
#     Y = np.array([1, 400, 800, 1300])
#     
#     df = pd.DataFrame({"X" : X, "Y" : Y})
#     
#     reg = smf.ols("Y ~ X", data = df)
#     model = reg.fit()
#     
#     print(model.summary())
#     print(model.params)
#     print(model.rsquared)
# 
# summary()
# =============================================================================
def fertilizer():
    np.random.seed(0)
    fart = np.array([1]*10 + [2]*10 + [3]*10)
    
    height = np.array(np.random.normal(loc = 10, scale = 2, size = 10).tolist() +
                      np.random.normal(loc = 12, scale = 2, size = 10).tolist() +
                      np.random.normal(loc = 14, scale = 2, size = 10).tolist())
    dataframe = pd.DataFrame({"Fertilizer" : fart, "Height" : height})
    
    anova = smf.ols("Height ~ C(Fertilizer)", data = dataframe).fit()
    
    anova_table = sm.stats.anova_lm(anova, typ=2)
    print(anova_table)
    turkey = pairwise_tukeyhsd(endog = dataframe["Height"], groups = dataframe["Fertilizer"])
    print("\nTukey's HSD Test Results")
    print(turkey.summary())
fertilizer()

