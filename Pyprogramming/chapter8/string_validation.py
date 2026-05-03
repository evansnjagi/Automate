# String validation

age = input("Enter your age: ")
username = input("Enter your user name: ")

# Input validation
if not age.isdecimal():
    print("Invalid age. Must be numeric.")
elif not username.isalnum():
    print("Invalid user name. Letters and numbers only.")
else:
    print("Valid input")