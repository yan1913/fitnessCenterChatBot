from twilio.rest import Client
account_sid = 'AC56ac5cf2f5d4673750dd02063d836b7c'
auth_token = '8d344743b1a290d19b362bbd2342bb64'
client = Client(account_sid, auth_token)

def fun():
    inputNum = input("Please enter your phone number")
    phoneNum = "44" + inputNum
    message = client.messages.create(
        from_='441865920701',
        body='Congratulations, the registration was successful.'
             'Thank you for updating your fitness center account details.'
             'We will send you the activity information and discount information in time. ',
        to=phoneNum
    )
    print(message.sid)

