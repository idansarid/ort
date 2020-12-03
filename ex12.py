

def find_max(x=1, y=1, z=1, b=1):
    max = 0
    arr = [x, y, z, b]
    for num in arr:
        if num > max:
            max = num
    return max


if __name__ == '__main__':
    x = int(input("Please enter an integer1: "))
    y = int(input("Please enter an integer1: "))
    z = int(input("Please enter an integer1: "))
    b = int(input("Please enter an integer1: "))
    print(find_max(x,y,z,b))