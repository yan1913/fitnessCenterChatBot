from twilio.rest import Client

## The following code is adapted from this example or video : https://www.twilio.com/docs/sms/quickstart/python-msg-svc
# I changed the account_sid and auth_token value to mach my API
account_sid = 'AC56ac5cf2f5d4673750dd02063d836b7c'
auth_token = '8d344743b1a290d19b362bbd2342bb64'
client = Client(account_sid, auth_token)



def fun():
    # I changed line 12 to 20 to make the phone number can enter from terminal
    inputNum = input("Please enter your phone number")
    phoneNum = "44" + inputNum
    message = client.messages.create(
        from_='441865920701',
        # I adapted the body information
        body='Congratulations, the registration was successful.'
             'Thank you for updating your fitness center account details.'
             'We will send you the activity information and discount information in time. ',
        to=phoneNum
    )
    print(message.sid)
## The end of the code is adapted from this example or video : https://www.twilio.com/docs/sms/quickstart/python-msg-svc
