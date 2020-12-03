def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers

def smallest_num_in_list(list):
    min = 100000
    for a in list:
        if a < min:
            min = a
    return min

def multiply_list(items):
    tot = 1
    for x in items:
        tot *= x
    return tot


def remove_duplicates(lst):
    dup_items = set()
    uniq_items = []
    for x in lst:
        if x not in dup_items:
            uniq_items.append(x)
            dup_items.add(x)

    return uniq_items


# main
# x= 1
# dict1 = {"k1": 1, "k2": 2}
# print(sum_list([1,2,-8,4,5]))
# print(multiply_list([1,2,-8]))
# print(smallest_num_in_list([1, 2, -8, 0]))

d = {0:10, 1:20}
d1 = {"k1":10, "k2":20}
print(d)
d.update({2:30})
print(d)

a = [10, 20, 30,20,10,50,60,40,80,50,40]

new_a = remove_duplicates(a)
# new_a = list(set(a))
print(new_a)