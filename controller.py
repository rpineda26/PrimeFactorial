
from math import sqrt
import random
"""
    Author : Ralph Dawson G. Pineda
    Description: This file contains the algorithms for primality test and factorial.
""" 

"""
@definition: This function checks if a number is prime or not. Time Complexity: O(n)
@params:  num  -  the number to be checked
@returns: True  - the number is prime
          False - the number is not prime
"""
def naive_isPrime(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                # if the number is divisible by any number other than 1 and itself, it is not prime
                return False 
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
    
"""
@definition: This function checks if a number is prime or not. This is based on the Miller-Rabin primality test.
            This is a probabilistic algorithm that trades off certainty for speed. Time Complexity: O(k log^3 n)
            The probability for a false positive is 1/4^k.

@params:  num  -  the number to be checked
@returns: True  - if the number is prime
          False - if the number is not prime
"""
def optimized_isPrime(num):
    #0 and 1 are not prime numbers
    if num < 2:
        return False
    #2 and 3 are prime numbers
    if num < 4:
        return True
    #even numbers other than 2 are not prime
    if num % 2 == 0:
        return False
 
    #num_tests is a hyper parameter that can be adjusted to increase the accuracy of the algorithm
    #The higher the number of tests, the lower the probability of a false positive  
    num_tests = 5
    for i in range(num_tests):
        #randomly select a number between 2 and num-1
        a = random.randint(2, num-1)
        #check the congruence relation a^(num-1) mod num = 1
        #prime numbers satisfy this relation
        #there are some composite numbers that also satisfy this relation (Carmichael numbers)
        x = pow(a, num-1, num)
        if x == 1:
        #passes the primality test, test another random number
        #to decrease the probability of a false positive
      
        #check the congruence relation a^(2^j * (num-1)) mod num = -1
        #x is is initialized as a^(num-1) mod num
        #the loop below finds the value of x^(2^j) mod num for j = 1 to count
        #This serves as extra tests to decrease the probability of a false positive

        #n-1 is even as num is odd > 3
        #this loop terminates when temp is no longer divisible by 2
        #count is the number of times that n-1 is divisible by 2
            temp = num -1
            while temp % 2 == 0:
                if x == num-1:
                    break
                x = pow(x, 2, num)
                temp = temp // 2
        else:
            return False
    return True

def optimized_factorial(num):
    if num == 0: #base case 0! = 1
        return 1
    else:
        factorial = 1
        for i in range(1, num+1):
            factorial *= i
        return factorial #iterative case
