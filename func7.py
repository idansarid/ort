# Built in functions


def ex5(x=-1):
    if all([x % 2 != 0, x > 0]):
        print("WIERD\n")
    elif all([x % 2 == 0, (x in range(1, 101))]):
        print("Not WIERD\n")
    elif x % 2 == 0 and (x in range(100, 1000)):
        print("Cool\n")
    elif x % 2 == 0 and x > 1000:
        print("Awsome\n")
    else:
        print("Idan is the king\n")


ex5(x=50)