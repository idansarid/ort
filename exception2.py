while True:
    try:
        x = int(input("Please enter a number: "))
        y = int(input("Please enter a number: "))
        x = x + 1
        z = x / y
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    except ZeroDivisionError:
        print("Oops!  That was no valid number.  Try again...")