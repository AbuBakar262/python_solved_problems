"""
    Factorial of number....
"""

def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact = fact * i
    return fact

print(f"Factorial of {5} is ", factorial(5))


"""
    Factorial of a list....
"""

def factorial_list(num_list):
    fact = 1
    fact_list = []
    for i in num_list:
        for j in range(1, i+1):
            fact = fact * j
        fact_list.append(fact)
        fact = 1
    return fact_list

print(factorial_list([1, 2, 3, 4]))