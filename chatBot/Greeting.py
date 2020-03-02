from nltk import word_tokenize
import random

greetings = ['hola', 'hello', 'hi', 'Hi', 'hey!', 'hey']
greetingAns = ["Hi there, cam I help you?", "May I help you?", "Do you need any help?", "What I can do for you?"]

questionHoliday = ['break', 'holiday', 'vacation', 'weekend']
responsesHoliday = ['It was nice! I went to Paris', "Sadly, I just stayed at home", ]

questionRegister = ["new user", "join in", "sing in", "Sing in", "Sing", "sing", "Login", "Log in", "login",
                    "new member"]
content=["content"]



    # 机器人跑起来

    # while True:
    #     userInput = input(">>> ")
    #     # 清理一下输入，看看都有哪些词
    #     cleaned_input = word_tokenize(userInput)
    #     # 这里，我们比较一下关键词，确定他属于哪个问题
    #     if not set(cleaned_input).isdisjoint(greetings):
    #         print(random.choice(greetingAns))
    #     elif not set(cleaned_input).isdisjoint(questionHoliday):
    #         print(random.choice(responsesHoliday))
    #     # 除非你说“拜拜”
    #
    #
    #
    #     elif userInput == 'bye':
    #         break
    #     else:
    #         print("I did not understand what you said")

    # >>> hi
    # hey
    # >>> how was your holiday?
    # It was nice! I went to Paris
    # >>> wow, amazing!
    # I did not understand what you said
    # >>> bye
