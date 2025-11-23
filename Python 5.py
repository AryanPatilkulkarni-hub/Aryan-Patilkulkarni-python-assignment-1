"""
5.	Design a module math_utils.py with functions:
factorial(n)
is_prime(n)
gcd(a,b)
Include exception handling for invalid or negative inputs. Import and test these functions from another script.
Concepts: Loops, recursion, functions, input validation.

"""

# math_utils.py

def factorial(n):
    """Return the factorial of n with input validation."""
    try:
        n = int(n)
    except ValueError:
        raise ValueError("Factorial: Input must be an integer.")

    if n < 0:
        raise ValueError("Factorial: Input must be non-negative.")

    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact


def is_prime(n):
    """Return True if n is prime, False otherwise."""
    try:
        n = int(n)
    except ValueError:
        raise ValueError("Prime check: Input must be an integer.")

    if n < 2:
        return False

    from math import sqrt
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def gcd(a, b):
    """Return the greatest common divisor of a and b."""
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        raise ValueError("GCD: Inputs must be integers.")

    if a < 0 or b < 0:
        raise ValueError("GCD: Inputs must be non-negative.")

    while b != 0:
        a, b = b, a % b
    return a

