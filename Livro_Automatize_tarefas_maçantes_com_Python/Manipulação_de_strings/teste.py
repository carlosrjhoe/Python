while True:
    age = input("Enter your age: ")
    if age.isdecimal():
        break
    else:
        print("Please enter a number for your age")

while True:
    password = input("Enter your password(letters and numbers only): ")
    if password.isalnum():
        break
    else:
        print("Passwords can only have letters and numbers")