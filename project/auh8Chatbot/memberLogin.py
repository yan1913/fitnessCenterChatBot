import csv
import sys
import random

from collections import defaultdict

# make a function


Name = list()
userID = list()
UserPassword = list()
with open('marks_test.csv', newline='\n') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        Name.append(row[0])
        userID.append(row[1])
        UserPassword.append(row[2])


def check_User_Info(user_input1, user_input2):
    for member_index in range(len(userID)):
        member_userID = userID[member_index]
        member_userPassword = UserPassword[member_index]
        member_name = Name[member_index]

        for elem in userID:
            if user_input1 == elem:
                print("Correct UserID.")
                member_index = userID.index(user_input1)

                if user_input2 == UserPassword[member_index]:
                    print("welcome!")
                    return True
                else:
                    print("your password or UserID is not valid, please try again")
                    return False


def isMember():
    while True:
        user_input1 = input("Please enter userID:")
        user_input2 = input("Please enter your password")
        y = check_User_Info(user_input1, user_input2)
        if y == True:

            break
        else:
            temp=input('''your password or UserID is not valid, please try again,
if you wanna exit the login system,please enter"No",if you wanna login again,
please press "return" to be continue''')
            if temp.lower()=="no":
                break
            else:
                continue
    return y




































