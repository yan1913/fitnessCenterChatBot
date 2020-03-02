from chatBot import BMIdemo
from chatBot.Register import ManageAccount
from chatBot import Greeting
from nltk import word_tokenize
import random

while True:
    userInput = input(">>> ")
    cleaned_input = word_tokenize(userInput)
    if not set(cleaned_input).isdisjoint(Greeting.greetings):
        print(random.choice(Greeting.greetingAns))
    elif not set(cleaned_input).isdisjoint(Greeting.questionHoliday):
        print(random.choice(Greeting.responsesHoliday))
    elif not set(cleaned_input).isdisjoint(Greeting.content):
        print("=====mainMenu=====")
        print("1.fitness suggestion")
        print("2.sport booking")
    elif not set(cleaned_input).isdisjoint(Greeting.questionRegister):
        print("=========REGISTER=========")
        userName = input("Enter your Username:")
        password = input("Enter your password:")
        gander = input("What is your gender:")
        age = input("How old are you:")
        weight = float(input("please enter your weight(kg):"))
        height = float(input("please enter your height:"))
        member = ManageAccount(userName, password, gander, age, weight, height)
        calculateBMI = BMIdemo
        print("==============your detail==============")
        print('username:', member.username)
        print('gander:', member.gander)
        print('age:', member.age)
        print('weight:', member.weight)
        print('height:', member.height)
        print("=======================================")
        res = input("Do you want to calculate your BMI and your health condition(yes/no):")
        if res == "yes":
            print("Your health result")
            BMI = BMIdemo.calBMI(member.weight, member.height)
            print("BMI:", BMI)
            print(BMIdemo.fun(BMI))
            print("=======================================")
            print("Do you need fitness advice)")

        else:
            print("Thank you, have a good day.")
            break

