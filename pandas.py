# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 08:29:31 2024

@author: engeb
"""
from pandas import Series, DataFrame

import pandas as pd
"""
obj = Series([4, 7, -5, 3])
print(obj)
print(type(obj))

print(obj.index)
print(obj.values)
"""
# =============================================================================
# print()
# print("Class Activity 1")
# print()
# import numpy as np
# 
# random_numbers = np.random.randint(1, 100, size = 10)
# obj_rand = Series(random_numbers, index = range(1,11))
# print(obj_rand)
# obj_rand_squared = obj_rand**2
# 
# great_numbers = obj_rand_squared[obj_rand_squared > 500].tolist()
# print(great_numbers)
#     
# 
# =============================================================================

"""
sdata = {"Texas": 10, "Ohio": 20, "Oregon":015, "Utah": 18}
states = ("Texas", "Ohio", "Oregon", "Iowa")
obj1 = Series(sdata, index=states)
#print(obj1)

#obj1.index = ["Florida", "New York", "Kentucky", "Georgia"]
#print(obj1)
obj1.index[2] = "California"
print(obj1)
"""

#DataFrame
#Tabular data structure
# =============================================================================
# 
# data = {"State": ["Ohio","Ohio", "Ohio","Nevada","Nevada"], 
#         "Year": [2000, 2001, 2002, 2001, 2002], 
#         "Pop":[1.5, 1.7, 3.6, 2.4, 2.9]}
# frame = DataFrame(data)
# 
# print(frame)
# 
# frame2 = DataFrame(data, columns = ["Year", "State", "Pop", "Debt"], 
#          index = ["A","B","C","D","E"])
# 
# print(frame2)
# =============================================================================

#Activity 2
# =============================================================================
# 
# data = {"Price" : [1600.20, 1610.02, 1618.07],
#         "Factor_1" : [1.255, 1.258, 1.249], 
#         "Factor_2" : [1.548, 1.554, 1.552]}
# 
# Frame = DataFrame(data)
# mean_factor_1 = Frame["Factor_1"].mean()
# standard_factor_1 = Frame["Factor_1"].std()
# 
# mean_factor_2 = Frame["Factor_2"].mean()
# standard_factor_2 = Frame["Factor_2"].std()
# 
# print(Frame)
# print()
# print("The mean for factor 1 is", mean_factor_1)
# print()
# print("The standard deviation for factor 1 is", standard_factor_1)
# print()
# print("The mean for factor 2 is", mean_factor_2)
# print()
# print("The standard deviation for factor 2 is", standard_factor_2)
# =============================================================================

#importing CSV files

# =============================================================================
# data_grades = pd.read_csv("Grades_Short.csv")
# 
# print(data_grades.head())
# print(data_grades.shape)
# print(data_grades.dtypes)
# print(data_grades.columns)
# print(data_grades.index)
# 
# print()
# print(data_grades[["Name", "Grade", "Mini_Exam3"]])
# print()
# 
# name = data_grades["Name"]
# print(name[3])
# print(name[1:4]) #non inclusive
# print(name[[1,2,4]]) #inclusive
# 
# slice1 = data_grades.loc[0:2, "Name":"Mini_Exam2"]
# print()
# print(slice1)
# 
# slice1 = data_grades.loc[[0,2,4,5], ["Name","Grade"]]
# print()
# print(slice1)
# 
# mean_final = data_grades["Final"].mean()
# 
# print()
# print(mean_final)
# 
# print()
# data_grades["Man"] = 1
# 
# print(data_grades.head())
# 
# data_grades.loc[0, "Man"] = 10
# 
# print(data_grades)
# 
# data_grades["Final_Percentage"] = data_grades["Final"]/36
# 
# print(data_grades.head())
# 
# #del data_grades["Man"]
# #print(data_grades)
# 
# data_grades.drop(["Man", "Final_Percentage"], axis = 1, inplace = True)
# 
# print(data_grades.head())
# =============================================================================

#Acitivty 3

data_values = pd.read_csv("values.csv")
print(data_values)

factor_1_mean = data_values["factor_1"].mean()
factor_1_standard = data_values["factor_1"].std()

print("Mean :", factor_1_mean)
print("Standard Dev: ", factor_1_standard)


data_values["factor_3"] = data_values["factor_1"]*3

print(data_values)


# =============================================================================
# data_parking = pd.read_csv("Parking.csv", index_col = 0,\parse_dates = ["Issue_Date"])
# 
# print(data_parking)
# =============================================================================

