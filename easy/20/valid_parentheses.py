def isValid(s: str) -> bool:
    parenthese_dict = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    stack = ["END"]

    # 長さが1の場合と奇数の場合
    if len(s) == 1 or len(s) % 2 == 1:
        return False

    for char in s:
        if char in parenthese_dict:
            # ペアとなる括弧をスタック
            stack.append(parenthese_dict[char])
        else:
            # 閉じ括弧を取得する
            pair_parenthese = stack.pop()
            if pair_parenthese == "END" or char != pair_parenthese:
                return False

    return len(stack) == 1


# s = "()"
# s = "())"
# s = "()[]{}"
# s = "(]"
# s = "(("
# s = "))"
print(isValid("()"))
