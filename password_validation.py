password = input("Enter a password: ")

def password_check(passw):
    special_symbol = ['$', '@', '#', '%']
    val = True

    if len(passw) < 6:
        print("Password Length should be atleast 6")
        val = False
    elif len(passw) > 20:
        print("Length should be less than 20")
        val = False
    elif not any(char.isdigit() for char in passw):
        print("Password should have atleast on number")
        val = False
    elif not any(char.isupper() for char in passw):
        print("Password should have one uppercase letter")
        val = False
    elif not any(char.islower() for char in passw):
        print("Password should have one lowercase letter")
        val = False
    elif not any(char in special_symbol for char in passw):
        print("Password should have atleast one special symbol")
        val = False
    else:
        return val


def main():
    if password_check(password):
        print("Password is valid")
    else:
        print("Password is invalid")


if __name__ ==  '__main__':
    main()
