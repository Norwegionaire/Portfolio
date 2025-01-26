# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 09:21:16 2024

@author: engeb
"""

print("ask the user three times for number\n")

a = 2
b = 3
c = b
b = a
a = c
print(a)
print(b)

n = int(input("Gib Numbah"))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if n < 0:
    print("fuck off")
else:
    print(factorial(n))
    
b = [1, 2, 3, 4]
a = b

a.append(5)

print(a)
print(b)

# A PROGRAM THAT IDENTIFIES EVEN NUMBERS
"""
def even_check():
    even = int(input("gib Numbah"))
    if even %2 == 0:
        print("this is even")
    else:
        print("this is odd")
"""

def count_even():
    even_list = []
    odd_list = []
    for i in range(101):
        if i %2 == 0:
            even_list.append(i)
        else:
           odd_list.append(i)
    print(sum(even_list))
    return even_list, odd_list

count_even()


import math


list1 = [9, 32, 37, 32, 20, 24, 10, 15, 21, 30]

#Function for Mean
def mean(numbers):
    #if the list is empty, the entire function outputs zero
    if len(numbers) == 0:
        return 0
    #counts the elements of the list
    n = len(numbers)
    #adding together the elements of the list
    sum_of = sum(numbers)
    #divides the sum of the elements with the number of elements
    mean_value = sum_of / n
    return mean_value

#function for variance
def variance(numbers):
    n = len(numbers)
    #inputs the mean function
    var_mean = mean(numbers)
    
    sqrd_diff = sum((i - var_mean)**2 for i in numbers) 
    variance_val = sqrd_diff/(n-1)
    return variance_val

#function for standard Deviation
def standard_deviation(numbers):
    var = variance(numbers) #sample variance
    deviation = math.sqrt(var) #Square root of variance
    return deviation


print(mean(list1))
print(standard_deviation(list1))
print()
print("task 8.11")
print()
def confidence_interval():
    n = 25
    mean_value = 30
    standard_error = 4/math.sqrt(n)
    #with a confidence interval of 95% has a z score of 1.96
    Z_score = 1.96
    lower_bounds = mean_value - Z_score * standard_error
    upper_bounds = mean_value + Z_score * standard_error
    return lower_bounds, upper_bounds

print(confidence_interval())


z = (64.24 - 62.6)/(2.88/math.sqrt(25))

print(z)