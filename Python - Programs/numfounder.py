"This program finds the location of a phone number and it's carrier"

# importion neede
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

# variables neede
num = input("Enter number with area code: ") # asks the user number with it's area code
p_num = phonenumbers.parse(num, "CH")
ser_num = phonenumbers.parse(num, "RO")

# printing process
print(geocoder.description_for_number(p_num, "en"))
print(carrier.name_for_number(ser_num, "en"))