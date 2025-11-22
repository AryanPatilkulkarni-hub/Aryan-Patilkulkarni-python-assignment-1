"""
5.	Design a module math_utils.py with functions:
factorial(n)
is_prime(n)
gcd(a,b)
Include exception handling for invalid or negative inputs. Import and test these functions from another script.
Concepts: Loops, recursion, functions, input validation.

"""

def factorial(n):
    try:
        n = int(n)
    except:
        print("Please enter the correct data type")
        return
    if n < 0:
        print("Please enter a positive integer")
        return
    if n == 0 or n == 1:
        print("Factorial is 1")
        return
    fact = 1
    for i in range(2,n+1):
        fact = fact*i
    print(f"Factorial is : {fact}")
    return


def is_prime(n):
    try:
        n = int(n)
    except:
        print("Please enter the correct data type")
        return
    if n < 0:
        print("Please enter a positive integer")
        return
    if n >= 0 and n < 2:
        print("Number is not prime")
        return
    for i in range(2,n):
        if n % i == 0:
            print("Number is not prime")
            return
    print("Number is prime")
    return

def gcd(a, b):
    try:
        a = int(a)
        b = int(b)
    except:
        print("Please enter the correct data type")
        return
    if a < 0 or b < 0:
        print("Please enter positive integers")
        return
    while b != 0:
        a, b = b, a % b
    print(f"GCD is : {a}")
    return
