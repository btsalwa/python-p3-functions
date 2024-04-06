#!/usr/bin/env python3

def greet_programmer(name="programmer"):
  print(f"Hello, {name}!")


def greet(name2="Guido"):
    print(f"Hello, {name2}!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")


def add(num1, num2):
    
    return num1 + num2

def halve(number):
    if not isinstance(number, (int, float)):
        return None
    
    return number / 2
    
