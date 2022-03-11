"This program finds the location of a phone number and it's carrier"
# importion needed
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import carrierdata

# variables neede
num = input("Enter number with area code: ") # asks the user number with it's area code
p_num = phonenumbers.parse(num, "CH")
ser_num = phonenumbers.parse(num, "RO")

# location and carrier
location = geocoder.description_for_number(p_num, "en")
carrier = carrier.name_for_number(ser_num, "en")
if carrier == "":
    carrier = 'Not found'

# printing process
print(f'{num} is located in {location}')
print(f'The carrier of {num} is {carrier}')