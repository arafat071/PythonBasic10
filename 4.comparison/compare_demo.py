def login():
    name = str(input("Input Your Name: "))
    password = int(input("Input Your Password:"))
    if name == "abc" and password == 12345:
        print("Login Successful")
    else:
        print("Error")


login()
