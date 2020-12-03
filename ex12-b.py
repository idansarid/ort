

def find_max(arr):
    max = 0
    for num in arr:
        if num > max:
            max = num
    return max


if __name__ == '__main__':
    x = 0
    input_arr = list()
    while x != -1:
        x = int(input("Please enter an integer1: "))
        if x != -1:
            input_arr.append(x)
    print(find_max(input_arr))