from datetime import datetime

now = datetime.now()

formatted_time = now.strftime("%m/%d/%Y %H:%M:%S")

print("Formatted Date and Time:", formatted_time)

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

import my_module

num = 5
print(f"Factorial of {num} is {my_module.factorial(num)}")
