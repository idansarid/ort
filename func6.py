

def sum(*args):
    total = 0
    for arg in args:
        total += arg
    print("total inside function: ", total)
    return total

sum(1,2,3,4,5,6,7,8,9,10,11,12)