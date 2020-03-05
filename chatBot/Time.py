import time

# Formatted into 2016-03-20 11:45:39
def localTime():
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))