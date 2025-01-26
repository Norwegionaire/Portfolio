#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:39:22 2024

@author: abbas
"""

# Import the math_utils and string_utils modules

import math_utils
import string_utils


# Get numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform mathematical operations
result_add = math_utils.add(num1, num2)
result_multiply = math_utils.multiply(num1, num2)

# Get a string from the user
user_string = input("Enter a string: ")

# Perform string operations
uppercase_string = string_utils.to_uppercase(user_string)
reversed_string = string_utils.reverse_string(user_string)

# Print the results
print(f"\nAddition Result: {result_add}\n")
print(f"Multiplication Result: {result_multiply}\n")
print(f"Uppercase String: {uppercase_string}\n")
print(f"Reversed String: {reversed_string}")


    
    



