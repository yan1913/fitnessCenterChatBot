from chatBot import BMIdemo
from chatBot import Register
from chatBot.Register import ManageAccount
from chatBot import Greeting
from chatBot import Weather
from chatBot import Time
from nltk import word_tokenize

import random

while True:
    userInput = input(">>> ")
    cleaned_input = word_tokenize(userInput)
    if not set(cleaned_input).isdisjoint(Greeting.greetings):
        print(random.choice(Greeting.greetingAns))
    elif not set(cleaned_input).isdisjoint(Greeting.questionHoliday):
        print(random.choice(Greeting.responsesHoliday))
    elif not set(cleaned_input).isdisjoint(Greeting.questionRegister):

        print("=========REGISTER=========")
        userName = input("Enter your Username:")
        password = input("Enter your password:")
        gander = input("What is your gender:")
        age = input("How old are you:")
        weight = float(input("please enter your weight(kg):"))
        height = float(input("please enter your height:"))

        member = ManageAccount(userName, password, gander, age, weight, height)
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
            BMI=BMIdemo.calBMI()
            print("BMI:", BMI)
            print(BMIdemo.fun(BMI))
            print("=======================================")
            print(random.choice(Greeting.greetingAns))
        else:
            print(random.choice(Greeting.greetingAns))
    elif not set(cleaned_input).isdisjoint(Greeting.questionLogin):
        print("RUN THE LOGIN FUNCTION ON HEAR")
        # if loginFunction==True:
    elif not set(cleaned_input).isdisjoint(Greeting.questionSuggestion):
            print("RUN THE FITNESS SUGGESTION FUNCTION ON HEAR")
        # "REGISTER OR LOGIN AGAIN"
    elif not set(cleaned_input).isdisjoint(Greeting.questionWeather):
        Weather.searchWeather()
    elif not set(cleaned_input).isdisjoint(Greeting.questionTime):
        Time.localTime()
    elif userInput=="bye" or userInput=="no":
        print("Thank you for using it.Have a good day")
        break

    else:
        print("Sorry, I don't understand.")