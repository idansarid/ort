
lst1 = [10, 20, 30] #global variable


def changeme(lst1):
    lst1 = [1, 2, 3, 4] # local variable
    print("the values inside lst1 are:", lst1)


changeme(lst1)
print("the values outside of the function are:", lst1)
