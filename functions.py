def add(a, b):
    return a + b

def subtract(a, b):
    return a - b  # <--- fix this in step 7

def multiply(a, b):
    return a * b

def convert_fahrenheit_to_celsius(fahrenheit):
    celsius= multiply(subtract(fahrenheit, 32), 5 / 9) # <-- Fix this in step 7
    assert celsius >= -273.15
    return celsius