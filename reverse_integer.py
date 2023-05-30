def reverse_number(num):
    reversed_number = 0
    while num !=0:
        digit = num % 10
        reversed_number = reversed_number * 10 + digit
        num //= 10
    return reversed_number


print(reverse_number(123))