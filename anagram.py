inp1 = "listenssss"
inp2 = "silsssentss"

if len(inp1) != len(inp2):
    print("Not an anagram")
    exit()


dict1 = {}
dict2 = {}

for i in inp1:
    if i in dict1:
        continue
    else:
        dict1[i] = inp1.count(i)

for i in inp2:
    if i in dict2:
        continue
    else:
        dict2[i] = inp2.count(i)

if dict1 == dict2:
    print("Anagram")
else:
    print("Not an anagram")
