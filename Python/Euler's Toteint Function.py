# This is a program to operate euler's toteint function.

import math

"""
What is a euler's toteint function??
Th function is represented as the greek letter Phi with a given parameter n where n is any real integer.
The totient function gives the number of all the numbers smaller than and coprime to n.

example: phi(2) = 1 {only 1}, phi(13) = 12 { 1 to 12 since 13 is a prime number}, phi(6) = 2 {1 and 5 only}, etc.  

for more info visit, https://brilliant.org/wiki/eulers-totient-function/
"""


# recieving the number n from user end
# n = int(input('Give a whole number:     '))

# the euler's function
def φ(number):
    """
    Function used to find the euler's totient function of the given number

    returns:
    tuple ===> (0: prime factors of the given number, 1: euler'stotient function answer)
    """

    # this is the function to find all the uniqe prime factors of the given number
    def primes(n=number):
        # now time to find all the prime factors of n
        primeFactors = [n]

        if n % 2 == 0:
            primeFactors.append(2)
        while n % 2 == 0:
            n = n / 2

        for i in range(3, math.floor(math.sqrt(n)) + 1):
            if n % i == 0:
                while n % i == 0:
                    n = n / i
                primeFactors.append(i)

        return primeFactors

    # this is the function to calculate the euler's multiplication method
    def eulerMult(answer=number, primes=primes(number)):
        # now we will us ethe euler's multiplication method to find the phi function
        for i in primes:
            answer = answer * (1 - 1 / (int(i)))
        return int(math.ceil(answer))

    # this function returns a tuple
    return primes(), eulerMult()


# this function will show you the formula used
def eulFunc(primes):
    string = ""
    for i in primes:
        string += f"(1 - 1/{i})"
    return string


# printing a table of the numbers, their euler's function and their formula/prime factors
for i in range(2, 100 + 1):

    # table with prime factors
    print(f"number: {i},    φ({i}) = {φ(i)[1]},    Prime Factors: {φ(i)[0] + [1]}")

    # table with the formula
    # print(f"number: {i},    φ({i}) = {φ(i)[1]},    formula: {str(i) + eulFunc(φ(i)[0])}")
