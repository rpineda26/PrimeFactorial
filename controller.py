
from math import sqrt
"""

    Author : Ralph Dawson G. Pineda
    Description: This file contains the algorithms for primality test and factorial.
    
""" 

"""
@definition: This function checks if a number is prime or not. Time Complexity: O(n)
@params:  num  -  the number to be checked
@returns: True  - if the number is prime
          False - if the number is not prime
"""
def naive_isPrime(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                return False # if the number is divisible by any number other than 1 and itself, it is not prime
        else:
            return True
    else: # 0 and 1 are not prime numbers
        return False
    

"""
@definition: This function computes the factorial of a number using a recursive approach. Time Complexity: O(n)
@params:  num  -  the number to be computed
@returns: 1 - base case when num is 0
        num * factorial(num-1) - recursive case
"""
def naive_factorial(num):
    if num == 0: #base case 0! = 1
        return 1
    else:
        return num * naive_factorial(num-1) #recursive case
