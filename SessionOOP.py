# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 08:31:42 2024

@author: engeb
"""
#all about efficiency
#they are a blueprint to share all the objects
#easier to organize classes
#avoid redundancy
# =============================================================================
# class Dog:
#     id = 0
#     name = "null"
#     age = 0
#     cert = " "
#     def printit():
#         print("Object is constructed")
# 
# dog1 = Dog()
# 
# dog1.id = 120
# dog1.name = "Max"
# dog1.age = 5
# dog1.printit()
# =============================================================================

# =============================================================================
# class human:
#     name = "Null"
#     age = 0
#     height = 0
#     weight = 0
#     gender = "Null"
# 
# laila = human()
# laila.name = "Laila"
# laila.age = 39
# laila.weight = 50
# 
# print(f"The name is {laila.name} and the age is {laila.age}")
# 
# =============================================================================

# =============================================================================
# class Student:
#     #this is a constructor function, 
#     #self means for every object that creates me
#     def __init__(self, name, age, grades):
#         self.name = name
#         self.age = age
#         self.grades = grades
#     
#     def introduce(self):
#         return f"My name is {self.name} and my age is {self.age} years old"
#     
#     def calculate_average(self):
#         return sum(self.grades) / len(self.grades)
#     
#     #def __del__():
# 
# #Have to ask for the diagram, so i can plan properly        
# 
# student1 = Student("Engebret", 24, [85, 90, 78])
# student2 = Student("Fredrik", 24, [88, 76, 95])
# =============================================================================

# =============================================================================
# class Car:
#     def __init__(self, brand, color, price, model_year):
#         self.brand = brand
#         self.color = color
#         self.price = price
#         self.model_year = model_year
#         
#     def car_model_info(self):
#         return(f"This car is the new {self.model_year} {self.brand}, it has a beautiful {self.color} finish.")
#     def car_model_price(self):
#         return(f"Certianly, the car costs {self.price} dollals")
#     
# ford = Car("Ford Focus", "Grey", 1999, 2008)
# porsche = Car("Porsche Macan", "Blue", 79999, 2024)
# merc = Car("Mercedes E-class", "Red", 49999, 2022)
# totoya = Car("Toyota Prius", "Black", 29999, 2023)
# 
# print(merc.car_model_info())
# ask = input("Would you like to see the price of this model? (y/n)")
# if ask == "y":
#     print(merc.car_model_price())
# elif ask == "n":
#     print("Have a nice day")
# else:
#     print("Fuck Off")
# =============================================================================

# =============================================================================
# class Dog():
#     def __init__(self, doginfo):
#         self.name = doginfo[0]
#         self.age = doginfo[1]
#         self.gender = doginfo[2]
#     
#     def dog_info(self):
#         return f"Meet {self.name}. He is {self.age} and is a very good {self.gender}"
#     def dog_humanage(self):
#         return f"{self.name} is {self.age*7} in human years"
# 
# dogs = [("Barko", 5, "boy"), ("Destroyer", 2, "girl"), ("Max Payne", "30-ish", "cop")]
# dog1 = Dog(dogs[0])
# dog2 = Dog(dogs[1])
# dog3 = Dog(dogs[2])
# 
# print(f"{dog1.dog_info()} and {dog1.dog_humanage()}.")
# print(f"{dog2.dog_info()} and {dog2.dog_humanage()}.")
# print(f"{dog3.dog_info()}.")
# 
# for n, a in dogs:
#     dog = Dog(n, a)
#     dogs.appned(dog)
# =============================================================================
#Adding instance of objects to a list

s = input("What")
count = 0
for i in s:
    if "0" <= i <= "9":
        count = count + 1
print(count)