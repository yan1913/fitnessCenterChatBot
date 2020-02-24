import re

# 1. At least 2 letter between [a-z]
# 2. At least 1 number between [0-9]
# 3. At least 1 letter between [A-Z]
# 4. At least 2 character from [$!#@]
# 5. Minimum length of transaction password: 8
# 6. Maximum length of transaction password: 16


# user_input = input("Please enter a password:")
# print("The requirements of your password:")


def check_password_validity(user_input):
    # Condition 1
    if len(re.findall(r'[a-z]', user_input)) < 2:
        print("Not Valid! The password should contain at least two characters of a-z")
        return False

    elif len(re.findall(r'[0-9]', user_input)) < 1:
        print("Not Valid! The password should contain at least one character of 0-9")
        return False

    elif len(re.findall(r'[A-Z]', user_input)) < 1:
        print("Not Valid! The password should contain at least one character of A-Z")
        return False

    elif len(re.findall(r'[$!#@]', user_input)) < 2:
        print("Not Valid! The password should contain at least two character of $!#@")
        return False

    elif len(user_input) < 8:
        print("Not Valid! The password should contain at least 8 characters")
        return False

    elif len(user_input) > 16:
        print("Not Valid! The password should contain no more than 16 characters")
        return False
    else:
        print("Welcome to join our membership!")
        return True

while True:
    user_input = input("Please enter a password:")
    a=check_password_validity(user_input)
    if a ==True:
        break

    # print("The requirements of your password:")

