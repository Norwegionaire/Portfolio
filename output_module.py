# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 13:22:24 2024

@author: engeb
"""

from dog_module import dogs
from input_module import dogInput
from conversion_module import dogAge, humanAge

dog = dogs()
dogName = dogInput()
#if the dog is in the list, then the code will print this line
def dogOutput():
    if dogName in dog:
        age = dogAge()
        age_human = humanAge()
        #the names are capitilized when reentered
        print(f"{dogName} is {age} years old, which is {age_human} in human years")
    else:
        print(f"{dogName}, isn't on the list. Try Again")
        
dogOutput()