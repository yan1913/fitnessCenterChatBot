from nltk import word_tokenize
import random

# Hello
greetings = ['hola', 'hello', 'hi', 'Hi', 'hey!','hey']
# GreetingAns
random_greeting = random.choice(greetings)

# Topic anout "holiday"
question = ['break','holiday','vacation','weekend']
# Holiday Ans
responses = ['It was nice! I went to Paris',"Sadly, I just stayed at home"]
# random ans
random_response = random.choice(responses)



# run
while True:
    userInput = input(">>> ")
    #clean the input and chouse the key word
    # 清理一下输入，看看都有哪些词
    cleaned_input = word_tokenize(userInput)
    #这里，我们比较一下关键词，确定他属于哪个问题
    # compare the keywords to determine which problem they belong to
    if  not set(cleaned_input).isdisjoint(greetings):
        print(random_greeting)
    elif not set(cleaned_input).isdisjoint(question):
        print(random_response)
    # Quit condition
    elif userInput == 'bye':
        break
    else:
        print("I did not understand what you said")

#output
# >>> hi
# hey
# >>> how was your holiday?
# It was nice! I went to Paris
# >>> wow, amazing!
# I did not understand what you said
# >>> bye
