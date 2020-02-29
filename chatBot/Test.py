from chatBot import BMIdemo
from chatBot.Register import ManageAccount

while True:
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
        # BMI = calBMI(member.weight,member.height)
        BMI = BMIdemo.calBMI(member.weight, member.height)
        print("BMI:", BMI)
        print(BMIdemo.fun(BMI))
        break
    else:
        print("Thank you, have a good day.")
        break
