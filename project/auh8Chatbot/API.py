import requests,json
import googlemaps
from itertools import tee
import csv



API_key = 'AIzaSyD5ZxX5MPs-9gPdBzA0iMMes5Ac3f0uzYM'
gmaps = googlemaps.Client(key=API_key)

Latitude = list()
Longitude = list()
phone_number = list()
with open ('marks_test.csv', newline='\n') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        Latitude.append(row[4])
        Longitude.append(row[5])
        phone_number.append(row[3])



def distance_calculator(user_input3):
    API_key = 'AIzaSyD5ZxX5MPs-9gPdBzA0iMMes5Ac3f0uzYM'
    gmaps = googlemaps.Client(key=API_key)
    ur1 = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=Seattle&destinations=San+Francisco&key=AIzaSyD5ZxX5MPs-9gPdBzA0iMMes5Ac3f0uzYM"
    for member_index in range(len(phone_number)):
        member_phone_number = phone_number[member_index]
        member_Latitude = Latitude[member_index]
        member_Longitude = Longitude[member_index]

        for elem in phone_number:
            if user_input3 == elem:
                print("Correct Phone Number.")
                member_index = phone_number.index(user_input3)
                return True
                
            if user_input3 not in phone_number:
                
                print("Incorrect Phone Number, Please try again")
                return False

def googleMapAPI():
    while True:
        user_input3 = input("Please enter your telephone number")
        x = distance_calculator(user_input3)
        member_index = phone_number.index(user_input3)
        if x == True:
            LatOrigin = Latitude[member_index]
            LongOrigin = Longitude[member_index]
            origins = (LatOrigin, LongOrigin)

            LatDest = (52.409313)
            LongDest = (-1.504783)
            destination = (LatDest, LongDest)

            result = gmaps.distance_matrix(origins, destination, mode='walking')["rows"][0]["elements"][0]["distance"][
                "value"]
            result_2 = (result / 1000)

            print("The distance between your home and Coventry Sport and Leisure Center is:", +(result_2), "mile")
            break
        else:
            print("Incorrect Phone Number, Please try again")
            continue




    
    
     

                
                
                
