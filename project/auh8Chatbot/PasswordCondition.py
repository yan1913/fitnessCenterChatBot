import re

# 1. At least 2 letter between [a-z]
# 2. At least 1 number between [0-9]
# 3. At least 1 letter between [A-Z]
# 4. At least 2 character from [$!#@]
# 5. Minimum length of transaction password: 8
# 6. Maximum length of transaction password: 16
def check_password_validity( password ) :
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

