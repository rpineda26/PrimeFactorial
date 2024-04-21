# About
Technical Assessment for Software Engineering Internship

Author: Ralph Dawson G. Pineda

Date: April 2024


Test if a number is prime and compute its factorial.

Programming Language used: Python

Instructions to run the program: 

## :rocket: clone the repository
After cloning, install the necessary pip packages for the GUI:

```
pip install -r requirements.txt
```
or 
```
pip3 install -r requirements.txt
```

After installing of the necessary dependencies, run program with:
```
python main.py
```
or
```
python3 main.py
```

## :trident:  How to use the program
1. the number input must be a non negative integer
2. the start button will be enabled when a valid input is registered
3. click the start button or press enter on the number input field to start the computation

## :rocket: Test the program
Run the defined automated tests with 
```
python test.py
```
- The tests for the primality functions use integers up to 1000.
- The test for factorial computation relies on comparing the actual results with the results from pythons math library factorial function.
- The test for naive factorial is limited to n= 998 due to pythons limit for recursive depth.
- optimized factorial can go beyond n=998