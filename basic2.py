# מימוש fruits count
# מצא את כל האינקסים במערך של בננה
# 0, 2, 5, 7
fruits = ['banana', 'apple', 'banana', 'kiwi', 'apple', 'banana', 'ananas', 'banana', 'banana']
list_len = len(fruits)
indexes = []
index = 0
while index < list_len:
    temp_index = fruits.index('banana', index)
    indexes.append(temp_index)
    index = temp_index + 1


print(len(indexes))
