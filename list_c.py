
squares = []
for i in range(0, 10, 1):
    squares.append(i * i)

print(squares)

#with list comprehension
squares = [i * i for i in range(10)]