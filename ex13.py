

def reverse_str1(string_input):
    return string_input[::-1]


def reverse_str2(s="default"):
    str = ""
    for i in s:
        str = i + str
    return str


def reverse_str3(s):
    if len(s) == 0:
        return s
    else:
        return reverse_str3(s[1:]) + s[0]


if __name__ == '__main__':
    print(reverse_str2("idan"))