x = int(input("Please enter an integer1: "))
if x % 2 != 0:
    print("WIERD\n")
elif x % 2 == 0 and (x in range(1, 101)):
    print("Not WIERD\n")
elif x % 2 == 0 and (x in range(100, 1000)):
    print("Cool\n")
elif x % 2 == 0 and x > 1000:
    print("Awsome\n")
else:
    print("Idan is the king\n")
