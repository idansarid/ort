dic1 = {1:10, 2:20}
dic2 = {3:30,4:40}
dic3 = {5:50, 6:60}
dic4 = {}
dic4.update(dic1)
dic4.update(dic2)
dic4.update(dic3)
print(dic4)

student1 = {'name': 'Omer',
            'age': 17,
            'address': 'Tel Aviv'}

student2 = {'name': 'Katia',
            'age': 17,
            'address': 'Ramat Gan'}

all_students = list()
all_students.append(student1)
all_students.append(student2)
print(all_students)

# all_students = set()
# all_students.add(student1)
# all_students.add(student2)
# print(all_students)