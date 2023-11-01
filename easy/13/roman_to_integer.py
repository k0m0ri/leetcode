def subtract(src: int, tar: int):
    return src - tar


def romanToInt(s: str):
    dic_roman_to_integer = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    # 1文字の時はすぐに返す
    if len(s) == 1:
        return dic_roman_to_integer[0]

    ans = 0
    i = 0
    while i < len(s) - 1:
        # I, X, Cの場合は次の文字を見て値を確定させる
        if ((s[i] == 'I' and s[i + 1] in ['V', 'X']) or
            (s[i] == 'X' and s[i + 1] in ['L', 'C']) or
                (s[i] == 'C' and s[i + 1] in ['D', 'M'])):
            ans += subtract(dic_roman_to_integer[s[i + 1]],
                            dic_roman_to_integer[s[i]])
            # 次の文字まで見たのでインデックスを2つ進める
            i += 2
        else:
            ans += dic_roman_to_integer[s[i]]
            i += 1

        # 最後の文字を加算する
        if i + 1 == len(s):
            ans += dic_roman_to_integer[s[i]]
        print(ans, i)
    return ans


# s = "III" output = 3
# s = "LVIII" output = 58
# s = "MCMXCIV"" output = 1994
print(romanToInt("MCMXCIV"))
