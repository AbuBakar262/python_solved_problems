
def func():
    print("Check Function")


def dec1(func):
    def exec():
        print("Before Function Call")
        func()
        print("After Function Call")
    return exec


func()


@dec1
def func_call():
    print("Function Call")

func_call()