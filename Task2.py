'''
Author: Syam Kumar KS
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
        o   Square root of the number
        o   Natural logarithm (log base e) of the number
        o   Sine of the number (in radians)
3.   Displays the calculated results.
'''
import math

# Prompt the user for a number
num = float(input("Enter a number: "))

# Calculations using math module
square_root = math.sqrt(num)    # squre root of num 
natural_log = math.log(num)      # natural log of num
sine_value = math.sin(num)       # Sine value of num
print("Square root:", square_root)
print("Logarithm:", natural_log)
print("Sine:", sine_value)