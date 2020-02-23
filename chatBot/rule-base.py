import random
# Greeting
greetings = ['hola', 'hello', 'hi', 'Hi', 'hey!','hey']
# GreetingAns
random_greeting = random.choice(greetings)

#Question
question = ['How are you?','How are you doing?']
# “I am fine”
responses = ['Okay',"I'm fine"]
# random choice
random_response = random.choice(responses)

# run
while True:
    userInput = input(">>> ")
    if userInput in greetings:
        print(random_greeting)
    elif userInput in question:
        print(random_response)
    # condition of to quit the while loop
    elif userInput == 'bye':
        break
    else:
        print("I did not understand what you said")
#output:
# >>> hi
# hey
# >>> how are u
# I did not understand what you said
# >>> how are you
# I did not understand what you said
# >>> how are you?
# I did not understand what you said
# >>> How are you?
# I'm fine
# >>> bye
