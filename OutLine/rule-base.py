import random
# greeting
greetings = ['hola', 'hello', 'hi', 'Hi', 'hey!','hey']
# random_greeting = random.choice(greetings)
question = ['How are you?','How are you doing?']
responses = ['Okay',"I'm fine","Good.","Not bad.","Actually,not very good."]
# random_response = random.choice(responses)
# run
while True:
    userInput = input(">>> ")
    if userInput in greetings:
        print(random.choice(greetings))
    elif userInput in question:
        print(random.choice(responses))
    elif userInput == 'bye':
        break
    else:
        print("I did not understand what you said")
