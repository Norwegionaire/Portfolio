# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 13:22:22 2024

@author: engeb
"""
import dog_module
from input_module import dogInput

dogName = dogInput()

dog = dog_module.dogs()


def dogAge():
    DAge = dog[dogName]
    return DAge
    
def humanAge():
    HAge = dog[dogName]*7
    return HAge