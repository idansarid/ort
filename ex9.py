

x = int(input("Please enter an integer1: "))
number = ""
lst1 = []
lst2 = []
for i in range(1, x+1):
    number += str(i)
    number += ','

print(number)
lst1 = number.split(',')
lst1.pop()
for item in lst1:
    lst2.append(int(item)*int(item))

pass