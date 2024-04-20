
from math import sqrt
"""

    Author : Ralph Dawson G. Pineda
    About: Technical Assessment for the position of Software Engineer Intern
    Todo checklist:     

    - [x] 1. Implement GUI for accepting input and displaying output
    - [x] 2. Implement primality test
    - [x] 3. Implement factorial computation
    - [x] 4. Documentation
""" 



"""
@definition: This function checks if a number is prime or not.
@params:  num  -  the number to be checked
@returns: True  - if the number is prime
          False - if the number is not prime
"""
def isPrime(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print(num,"is not a prime number")
                return False
        else:
            return True
    else:
        return False
"""
@definition: This function computes the factorial of a number.
@params:  num  -  the number to be computed
@returns: 1 - base case when num is 0
        num * factorial(num-1) - recursive case
"""
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)



def displayAction(state, input, string, head):
    print("Current State: "+state)
    print("Current Input: "+input)
    print("Word Input: " +string)
    print("head: "+head)

    main()