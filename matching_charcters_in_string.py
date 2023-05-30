name = 'abcdefabcabc'
duplicates = []

for i in name:
    if name.count(i) > 1:
        if i not in duplicates:
            duplicates.append(i)



print(duplicates)
