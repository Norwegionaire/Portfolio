# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 11:13:22 2024

@author: engeb
"""
#tic tac toe
row1 = ["( )","( )","( )"]
row2 = ["( )","( )","( )"]
row3 = ["( )","( )","( )"]
# find the winning conditions

def choices_X(choice):
    if choice == "1":
        row1[0] = "X"
    elif choice == "2":
        row1[1] = "X"
    elif choice == "3":
        row1[2] = "X"
    elif choice == "4":
        row2[0] = "X"
    elif choice == "5":
        row2[1] = "X"
    elif choice == "6":
        row2[2] = "X"
    elif choice == "7":
        row3[0] = "X"
    elif choice == "8":
        row3[1] = "X"
    elif choice == "9":
        row3[2] = "X"
    else:
        print("not a choice")

def choices_O(choice):
    if choice == "1":
        row1[0] = "O"
    elif choice == "2":
        row1[1] = "O"
    elif choice == "3":
        row1[2] = "O"
    elif choice == "4":
        row2[0] = "O"
    elif choice == "5":
        row2[1] = "O"
    elif choice == "6":
        row2[2] = "O"
    elif choice == "7":
        row3[0] = "O"
    elif choice == "8":
        row3[1] = "O"
    elif choice == "9":
        row3[2] = "O"
    else:
        print("not a choice")

while True:

    print(row1)
    print(row2)
    print(row3)

    choice1 = input("where do you want to put the x (1-9): ")
    choices_X(choice1)
    print(row1)
    print(row2)
    print(row3)
    choice2 = input("where do you want to put the o (1-9): ")
    choices_O(choice2)