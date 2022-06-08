"This program finds the location of a phone number and it's carrier"
# importion needed
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import carrierdata

# variables neede
print('\n WELCOME TO LOCATION AND CARRIER \v')

num = input("Enter number with area code: ") # asks the user number with it's area code
p_num = phonenumbers.parse(num, "CH")
ser_num = phonenumbers.parse(num, "RO")

# location and carrier
location = geocoder.description_for_number(p_num, "en")
carrier = carrier.name_for_number(ser_num, "en")

# if nothing is found
if location == "" and carrier == "":
    print('Sorry, there is no location and carrier associated with this phone number')
    print('The phone number probably does not exist, since nothing seems to be associated with it.')   
elif carrier != "" and location != "":
    print(f'{num} is located in {location}')
    print(f'The carrier of {num} is {carrier}')
else:
    if carrier == "" and location != "":
        print(f'{num} is located in {location}')
        carrier = 'Not Found'
        print(f'The carrier of {num} is {carrier}')