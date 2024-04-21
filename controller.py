
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
@definition: This function computes the modular exponentiation of a number using the binary exponentiation algorithm.
            The base is squared in each iteration and the exponent is halved until the exponent is 0. Time Complexity: O(log n)
            as n represented by the exponent is halved in each iteration.
@params:  base  -  the base number
            exponent - the power to be raised
            mod - the modulo value
@returns: res - the result of the modular exponentiation
"""
def power_binary(base, exponent, mod):
    base = base % mod
    res = 1
    if exponent == 0:
        return 1
    #recursive case
    while(exponent > 0):
        #if exponent is odd, then multiply once more with the base
        #note that the base is always squared in each iteration
        if exponent % 2 == 1:
            #This makes sure the result is always small enough to prevent overflow
            res = res*base % mod
        base = base * base % mod
        exponent = exponent // 2
    return res
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
        #check the congruence relation a^(num-1) mod num = 1, prime numbers satisfy this relation
        #there are some composite numbers that also satisfy this relation (Carmichael numbers) and cause false positives
        #It is necessary to use the binary exponentiation implementation for calculating the power of x^a
        #python's pow function uses binary exponentiation so I used it instead of implementing my own
        x = power_binary(a, num-1, num)
        if x == 1:
            #passes the primality test, test another number
            #to decrease the probability of a false positive
            #use continue to move on to the next iteration of the for loop
            continue

        #n-1 is even as num is odd > 3
        #this loop terminates when temp is no longer divisible by 2
        #keep checking if a^d mod n = 1 or a^(2^r * d) mod n = -1
        temp = num -1
        while temp % 2 == 0:
            if x == num-1:
                #passes the primality test, test another number
                #use break to exit the while loop
                break
            x = power_binary(x, 2, num)
            temp = temp // 2
        else:
            return False
    return True
"""
@definition: This function checks if a number is prime or not. This is based on the Miller-Rabin primality test.
            This is a deterministic algorithm that uses a set of bases to check if a number is prime. 
            The difference here is that the base used for testing is not randomized, the bases selected are the first 
            prime numbers. This is only deterministic under a certain bound of numbers. In this case, using the first 4
            prime numbers is enough to be deterministic in the range of python's 32bit integer
            Time Complexity: O(log^3 n)
"""
def optimized_isPrime_deterministic(num):
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
    bases = [2, 3, 5, 7]
    for i in range(len(bases)):
        #randomly select a number between 2 and num-1
        a = bases[i]
        if num == a:
            return True
        #check the congruence relation a^(num-1) mod num = 1, prime numbers satisfy this relation
        #there are some composite numbers that also satisfy this relation (Carmichael numbers) and cause false positives
        #It is necessary to use the binary exponentiation implementation for calculating the power of x^a 
        x = power_binary(a, num-1, num)
        if x == 1:
            continue
        #passes the primality test, test another number
        #to decrease the probability of a false positive

        #n-1 is even as num is odd > 3
        #this loop terminates when temp is no longer divisible by 2
        #count is the number of times that n-1 is divisible by 2
        temp = num -1
        while temp % 2 == 0:
            if x == num-1:
                break
            x = power_binary(x, 2, num)
            temp = temp // 2
        else:
            return False
    return True

"""
@definition: This method computes the factorial of n using a divide and conquer approach.
            Instead of recursively multiplying n times, two recursive calls will be called each iteration 
            to reduce the number of multiplications. The first recursive call gets the factorial of n/1 while 
            the other gets (mid +1) * (mid + 2) * ... * max. Time Complexity: O(log n)  as the size of n is repeteadly
            haved in each iteration.
"""
#DP is used as a memoization table to store the results of the recursive calls
DP = [0] * (1000000000)
def optimized_factorial(min = 1, max=1):
    #mid is used as the marker for the divide and conquer approach
    mid = (min + max) // 2
    #return the factor so the parent call can multiply it with the other factors
    if min == max:
        return min
    #base case may occur when
    if min > max:
        return 1
    

    #The memoization table can be accessed when min = 1 as the computation is a full factorial starting from 1 * 2 * ... * max
    #Note that the recursive call can multiply mid * mid +1 * ... * max which is not a complete factorial as it doesnt start with 1
    #This if block is reached when div_conq_multiply(min, mid) is called
    if min ==1:
        #check if the value of mid! already stored in the memoization table
        if DP[max]!=0:
            #print("I am called for memoization")
            #store the result for max! in the memoization table
            return DP[max]
        if DP[mid]!=0:
            #print("I am called for memoization")
            #store the result for max! in the memoization table
            DP[max] = DP[mid] * optimized_factorial(mid+1, max)
        else:
            #store the result for max! in the memoization table
            #note that mid! will also be stored in the memoization table because of the recursive call
            DP[max]= optimized_factorial(min, mid) * optimized_factorial(mid+1, max)
        return DP[max]
    else:
        #dont store the result in the memoization table as the computation is not a full factorial
        #this block is reached when div_conq_multiply(mid+1, max) is called
        return optimized_factorial(min, mid) * optimized_factorial(mid+1, max)
    
