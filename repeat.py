# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 18:51:51 2023

@author: nsamuel1
"""

# Ball.py

def calculate_max_height(v0, g):
    max_height = (v0 ** 2) / (2 * g)
    return max_height

# Input values from the console
v0 = float(input("Enter the initial velocity of the ball (ft/sec): "))
g = 32.8  # force of gravity in ft/sec^2

# Calculate maximum height
max_height = calculate_max_height(v0, g)

# Display the result
print(f"The maximum height reached by the ball is: {max_height} ft")