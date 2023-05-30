num = int(input("Enter a number : "))

if num == 0:
    print("Number is Zero")
elif 1 <= num <= 10:
    print("Number is between 1 - 10")
else:
    print("Number is greater than 10")

check = num if num == 0 else 1 <= num <= 10

print(check)
