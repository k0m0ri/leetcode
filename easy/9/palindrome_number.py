def isPalindrome(x: int) -> bool:
    if x < 0:
        return False

    str_x = str(x)
    re_str_x = ''
    for i in range(len(str_x) - 1, -1, -1):
        re_str_x += str_x[i]
    # 上記はstr(x)[::-1]で代替可能

    if str_x == re_str_x:
        return True
    return False


# x = 121, true
# x = -121, false
# x = 10, false
print(isPalindrome(10))
