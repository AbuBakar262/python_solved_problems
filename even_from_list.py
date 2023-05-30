list1 = [1,2,3,5,6,7,8,9,0,10]

evenlist = []

oddlist = []

for i in list1:
    if i%2==0:
        evenlist.append(i)
    if i%2!=0:
        oddlist.append(i)

print(sorted(evenlist + oddlist))