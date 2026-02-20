# Task 2 - Recursive Function: Factorial Utility

def factorial(n):
    if n < 0:
        print("Error: Factorial not defined for negative numbers.")
        return None
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# Test cases
print(factorial(5))   # Expected: 120
print(factorial(0))   # Expected: 1
print(factorial(-3))  # Expected: Error message