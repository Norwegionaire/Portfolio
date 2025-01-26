# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 13:50:10 2024

@author: engeb
"""
import pandas as pd

class Product():
    def __init__(self, i, n, p, q):
        self.id = i
        self.name = n
        self.price = p
        self.quiantity = q

class Inventory(Product):
    def __init__(self, i, n, q)