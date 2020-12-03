def isPalindrom(str="anna"):
    str = str.replace(" ", "")
    if str == str[::-1]:
        return True
    else:
        return False

# main

ans = isPalindrom(str="nurses run")
print(ans)