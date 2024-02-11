#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i >= 1:
        print(i)
        i -= 1
    print("Happy New Year!")



def square_integers(int_list):
    squared = []
    for num in int_list:
        squared_num = num ** 2
        squared.append(squared_num)
    return squared
    

def fizzbuzz():
    i = 1
    while i < 100: 
        print(i)
        i-=1
    if i % 3 == 0: 
        print("Fizz")
    elif i % 5 == 0:
        print ("Buzz")
    elif i % 5 == 0 and i % 3 == 0:
        print ("FizzBuzz")
    
