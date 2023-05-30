def hello_decorator(func):
    def innr():
        print("Before Executing Func")
        func()
        print("After Executing Func")
    return innr()

