import re

def check_password_validity(password):
    # Condition 1
    if len(re.findall(r'[a-z]', password)) < 2:
        print("Not Valid! The password should contain at least two characters of a-z")
        return False
    elif len(re.findall(r'[0-9]', password)) < 1:
        print("Not Valid! The password should contain at least one character of 0-9")
        return False
    elif len(re.findall(r'[A-Z]', password)) < 1:
        print("Not Valid! The password should contain at least one character of A-Z")
        return False
    elif len(re.findall(r'[$!#@]', password)) < 2:
        print("Not Valid! The password should contain at least two character of $!#@")
        return False
    elif len(password) < 8:
        print("Not Valid! The password should contain at least 8 characters")
        return False
    elif len(password) > 16:
        print("Not Valid! The password should contain no more than 16 characters")
        return False
    else:
        print("Welcome to join our membership!")
        return password

# while True:
#     user_input = input("Please enter a password:")
#     a=check_password_validity(user_input)
#     if a ==True:
#         break

    # print("The requirements of your password:")

