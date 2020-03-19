from project.auh8Chatbot import API
from project.auh8Chatbot import memberLogin
from project.liaoy19.Register import ManageAccount
from project.liaoy19 import Time, Greeting, Weather, Message, BMIdemo
from nltk import word_tokenize
from project.moham977 import fitness
from project.sondeo import groupexercises

import random

while True:
    userInput = input(">>> ")
    cleaned_input = word_tokenize(userInput)
    if not set(cleaned_input).isdisjoint(Greeting.greetings):  # Greeting function
        print(random.choice(Greeting.greetingAns))

    elif not set(cleaned_input).isdisjoint(Greeting.questionHoliday):  # Chatting about holiday
        print(random.choice(Greeting.responsesHoliday))

    elif not set(cleaned_input).isdisjoint(Greeting.questionRegister):  # Register a new member
        print("=========REGISTER=========")
        userName = input("Enter your Username:")
        password = input("Enter your password:")
        gander = input("What is your gender:")
        age = input("How old are you:")
        weight = float(input("please enter your weight(kg):"))
        height = float(input("please enter your height:"))
        member = ManageAccount(userName, password, gander, age, weight, height)
        print("registration was successful")
        print("==============your detail==============")
        print('username:', member.username)
        print('gander:', member.gander)
        print('age:', member.age)
        print('weight:', member.weight)
        print('height:', member.height)
        print("=======================================")
        messageAPI = input("Would you like to receive more relevant information via SMS?(yes/no)")  # Send
        # the"registers the success" confirmation message and get the root of phone number information
        if messageAPI == "yes":
            Message.fun()
        else:
            pass
        res = input("Do you want to calculate your BMI and your health condition(yes/no):")
        # get the BMI value and fitness suggestion
        if res == "yes":
            print("Your health result")
            BMI = BMIdemo.calBMI(member.weight, member.height)
            print("BMI:", BMI)
            print(BMIdemo.fun(BMI))
            print("=======================================")
            print(random.choice(Greeting.greetingAns))
        else:
            print(random.choice(Greeting.greetingAns))

    elif not set(cleaned_input).isdisjoint(Greeting.questionSuggestion): # the fitness suggestion.

        print("RUN THE FITNESS SUGGESTION FUNCTION RIGHT HERE")

    elif not set(cleaned_input).isdisjoint(Greeting.questionWeather): # get weather information
        Weather.searchWeather()

    elif not set(cleaned_input).isdisjoint(Greeting.questionGoogleMapAPI):
        # Get the distance from the location of the phone to the fitness center
        API.googleMapAPI()

    elif not set(cleaned_input).isdisjoint(Greeting.questionTime):
        # When asking the time, output the system time
        Time.localTime()

    elif not set(cleaned_input).isdisjoint(Greeting.questionLogin):
        loginStatus=memberLogin.isMember()
        # login function
    elif not set(cleaned_input).isdisjoint(Greeting.questionClass):
        fitness.fitness_classes()

    elif not set(cleaned_input).isdisjoint(Greeting.questionGroup):
        groupexercises.runFun()

    elif userInput == "bye" or userInput == "no":
        print("Thank you for using it.Have a good day")
        break
    else:
        print("Sorry, I don't understand.")

