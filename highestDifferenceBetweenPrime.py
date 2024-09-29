# I tried to find the greatest difference between two consecutive prime numbers.
# Just using some simple python while loops and importing the isprimt() lib from sympy.
# This is my first prime experiment as a first year student at TU Dublin

#WARNING : This will run an infinity loop, will stress your PC to some great extent.

#Author : Akshat Pasbola
#Date : 29 / 10 / 2024

from sympy import isprime

def  findnextPrime(input):
    t = input + 1
    while True:
        if isprime(t):
            return t
        t += 1
x = 1
highestNum = 0
while 1:
    y = findnextPrime(x)
    diff = y-x
    if diff > highestNum:
        highestNum = diff
        print(f"{y} - {x} = {highestNum}") # prints the highest difference between two consecutive primes
    x = y


