


total = 0

def sum(a,b):
    global total
    total = a + b
    print("total inside function: ",total)
    return total

sum(10,20)
print("total outside function: ", total)