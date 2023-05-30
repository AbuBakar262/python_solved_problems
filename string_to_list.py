name = 'AbuBakar'
mylist = []

for i in name:
    mylist.append(i)

print(mylist)

"""
    OR /// Another way
"""

county = 'Pakistan'
new_list = list(county)
print(new_list)
result = int(len(new_list) / 2)

print(result)

print(new_list[result])


"""
    Converting List In to String
"""

for i in mylist:
    x = ''.join(i)
    print(x, end='')
