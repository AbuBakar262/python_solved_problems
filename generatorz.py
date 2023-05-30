def gen_func():
    n = 1

    print("1st Execution")
    yield n

    n += 1
    print("2nd Execution")
    yield n


    n += 1
    print("3rd Execution")
    yield n


a = gen_func()

# 1st Execution
print(next(a))

# 2nd Execution
print(next(a))

# 3rd Execution
print(next(a))


# for item in gen_func():
#     print(item)
