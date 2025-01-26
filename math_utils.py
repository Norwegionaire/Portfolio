#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:38:18 2024

@author: abbas
"""


import helper_utils           # Importing the helper_utils module for validation


def add(a, b):
    """Add two numbers after validating them."""
    if helper_utils.is_number(a) and helper_utils.is_number(b):
        return a + b
    else:
        raise ValueError("Both inputs must be numbers")
        

def multiply(a, b):
    """Multiply two numbers after validating them."""
    if helper_utils.is_number(a) and helper_utils.is_number(b):
        return a * b
    else:
        raise ValueError("Both inputs must be numbers")

print("math_utils module has been imported.")