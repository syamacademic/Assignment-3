'''
Author: Syam Kumar KS
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.
'''

def factorial(no):
    '''
    Calculates the factorial of a given non-negative integer.

    The function returns the product of all positive integers less than
    or equal to the given number.

    Parameters:
    no (int): A non-negative integer whose factorial is to be calculated.

    Returns:
    int: Factorial of the given number if no >= 0.
    None: If the number is negative, since factorial is not defined.
    '''
    if no < 0:
        print("Factorial does not exist for negative numbers")
        return None
    elif no == 0:
        return 1
    else:
        # Initialize the factorial result and a counter
        result = 1
        i = 1
        # Loop from 1 up to and including n
        while i <= no:
            result *= i
            i += 1
        return result
if __name__ == "__main__":
    no = int(input("Enter a number: "))
    print(f"Factorial of {no} is : {factorial(no)}")
