# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 08:38:45 2024

@author: engeb
"""
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * self.radius **2

class ModCImport:
    def __init__(self):
        pass
    def printit(self):
        print("Hi")