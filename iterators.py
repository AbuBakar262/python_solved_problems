my_list = [1, 2, 3, 4, 5]

iter_obj = iter(my_list)

while True:
    try:
        print(next(iter_obj))
    except:
        break
