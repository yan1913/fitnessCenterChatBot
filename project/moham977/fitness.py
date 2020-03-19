import random
import requests
from project.moham977 import trainers
import pprint

def fitness_classes():
    rainers = ("\nName:Dave \nAge:35 \nContact:07498244991 \nGender:Male \nPrice:£50 "
               "\nDiscription: Fun and effective personal training.Discounted Six Week Promise package for new starters."
               "\n\n\nName:Dominic \nAge:42 \nContact:0794 117 9159 \nGender:Male \nPrice:£30"
               " \nDiscription:I have unique programme sessions to help support your well being and weightloss/fitness"
               "\n\n\nName:Caro \nAge:27 \nContact:07514002001 \nGender:Female \nPrice:£40 "
               "\nDiscription:Im Caro, a Personal Trainer.I Help people Lose Weight, Get Fit And Feel Great,"
               "\n\n\nName:Fiona \nAge:£40 \nContact:07575344473 \nGender:Female \nPrice:£40 \nDiscription:Hello! I’m Fiona - A friendly, experienced Personal Trainer and Holistic Lifestyle Coach dedicated to helping you look and feel your best."
               "\n\n\nName:Craig \nAge:30 \nContact:07932726450 \nGender:Male \nPrice:£30 \nDiscription:Over 19 years experience as a Personal Trainer, getting many new success stories.\n\n")

    intro = ["Welcome to the classes section, \nwe have various type of classes, "
             "\nwhich class would you like to join, \nwe have productive gym sessions, "
             "\ndifferent sports, dance classes \nand also we have yoga classes, \nThankyou.(enter'gym')",
             "Thanks for coming to our classes section. \nWhat section would you like to join today"
             " \nwe have amazing gym training classes, \ndifferent varieties of sports, "
             "\ndances classes and yoga classes also, \nThankyou.(enter'gym')",
             "This is the classes we have here at fitness center, \nand these are the classes we have,"
             "\n: GYM : SPORTS : DANCES : YOGA :, \n please choose from the list above, \nThankyou.(enter'gym')"]

    # trns is a personal file created

    # from trns import intro
    print("Here are some home workout videos to try.")
    workout = ("https://www.youtube.com/results?search_query=home+workout")
    print(workout)
    print(random.choice(intro))
    a = input()
    input1 = str(a.lower())
    if "gym" in input1:
        while True:
            print("Would you like a personal gym trainer or join a group gym class.(enter 'personal')")
            b = input()
            input2 = str(b.lower())
            if "personal" in input2:
                print("These are the lists of personal trainers we have, "
                      "\nplease use name to choose one below and proceed to payment.")
                print(trainers)
                while True:
                    input3 = input()
                    input3 = str(input3.lower())
                    if "dave" in input3:
                        image=requests.get("https://members.nrpt.co.uk/nrpttrainers/trainer-026470.jpg")
                        print(image)
                        print("The price is £50")
                        print("please call dave.")
                        break
                    elif "dominic" in input3:
                        image = requests.get("https://members.nrpt.co.uk/nrpttrainers/trainer-031683.jpg")
                        print(image)
                        print("The price is £30")
                        break
                    elif "caro" in input3:
                        image = requests.get("https://members.nrpt.co.uk/nrpttrainers/trainer-031705.jpg")
                        print(image)
                        print("The price is £40")
                        break
                    elif "fiona" in input3:
                        image = requests.get("https://members.nrpt.co.uk/nrpttrainers/trainer-028972.jpg")
                        print(image)
                        print("The price is £40")
                        break
                    elif "craig" in input3:
                        image = requests.get("https://members.nrpt.co.uk/nrpttrainers/trainer_1641.jpg")
                        print(image)
                        print("The price is £30")
                        break
                    else:
                        print("What you said was not in the list, "
                              "\nplease check the spelling of the name and type again."
                              "\n(enter'dave,dominic,caro,fiona or craig')"
                              )
                print("If you wanna get more information about group exercises,please enter something about 'group'.")
                break
            else:
                print("what you said was not in the options, please chose again.(enter'dave,dominic,caro,fiona or "
                      "craig')")


