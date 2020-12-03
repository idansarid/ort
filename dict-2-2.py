d1 = {}
d2 = {3:40, 5:60}
d3 = {6:33, 9:11}

print(len(d1))
d1.update({1:10})
d1.update({2:20})
print(d1)

unite = (d1, d2, d3)
print(type(unite))

united_d = {}
united_d.update(d1)
united_d.update(d2)
united_d.update(d3)
print(united_d)
del united_d[3]
print(united_d)
for k, v in united_d.items():
    print(k)

print("#######\n")
for k, v in united_d.items():
    print(v)


dic1 = {1:10, 2:20}
dic2 = {3:30,4:40}
dic3 = {5:50,6:60}
dic4 = {}
dic4.update(dic1)
dic4.update(dic2)
dic4.update(dic3)
print(dic4)