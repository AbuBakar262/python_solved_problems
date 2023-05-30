num = [1,2,3,4,5,6,7,8,9,10,11,12,13]

prime_list = []
even_list = []
for i in range(2, len(num)+1):
    if i % 2 != 0 and i / 3 != 0:
        if i % i == 0:
            prime_list.append(i)
    else:
        even_list.append(i)

print(prime_list)
print()
print(even_list)
