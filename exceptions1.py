x = int(input("Please enter an integer1: "))
y = int(input("Please enter an integer1: "))
try:
    z = x / y
except ZeroDivisionError as e:
    print("Illegal input!!!!!, please try again!\n")