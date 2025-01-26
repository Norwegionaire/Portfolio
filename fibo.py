# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 09:50:07 2024

@author: engeb
"""
def fib(n):
    a, b = 0, 1
    
    while b < n:
        print(b, end=" ")
        a, b = b, a+b
    print()

fib(50)