# CREATING ANOTHER SUB CLASS
crunches = "3pm daily"
weightlifting = "5pm daily"
yogaclass = "1pm daily"
salsaclass = "7pm daily"


# groupExerciseclasses(male,female)


def groupExerciseClasses(gender):
    exercises = [crunches, weightlifting, salsaclass, yogaclass]
    if gender == "male":
        print("crunches", crunches, "and", "weightlifting", weightlifting, "is avaliable")
        return ""
    elif gender == "female":
        print("yogaclass", yogaclass, "salsaclass", "and", salsaclass, "is avaliable")
        return ""
    else:
        return "impossible"


def runFun():
    while True:
        gender = input("PLEASE ENTER YOUR GENDER(if you wanna quit,please enter No):")
        groupExerciseClasses(gender)
        if gender == "No":
            break
