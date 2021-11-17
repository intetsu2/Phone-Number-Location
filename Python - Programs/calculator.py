# calicurator for addind, multiplying, minus, divingi, amd square roort

def add():
    num1 = int(input())
    num2 = int(input())
    ad_total = num1 + num2
    print (str(num1) + " + " + str(num2) + " = " + str(ad_total))

def minus():
    num1 = int(input())
    num2 = int(input())
    mn_total = num1 - num2
    print (str(num1) + " - " + str(num2) + " = " + str(mn_total))

while True:

    calic = input("Add, Minus, Multiply, Divide. Squareroot: ")

    if calic ==  "Add" or calic == "add":
        add()
    elif calic == "Minus" or calic == "minus":
        minus()
    