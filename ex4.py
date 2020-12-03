sum = 0
max_sum = 0
count = 0
x = int(input("Please enter an integer1: "))
y = int(input("Please enter an integer1: "))
while x != -1:
    count +=1
    if x % 2 == 0 and y % 2 != 0:
        sum = x + y
        if sum > max_sum:
            max_sum = sum
    x = int(input("Please enter an integer1: "))
    y = int(input("Please enter an integer1: "))