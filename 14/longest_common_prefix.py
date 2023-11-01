def indexOfMinLengthWord(strs: [str]) -> str:
    # 最大の文字数は200
    min_length = 999
    index = 0
    for i in range(len(strs)):
        word_length = len(strs[i])
        if min_length > word_length:
            min_length = word_length
            index = i
    return index


def longestCommonPrefix(strs: [str]) -> str:
    # strsが一単語のみならそのまま返す
    if len(strs) == 1:
        return strs[0]

    # strsの内、最も短い単語を探して配列から取り除く
    tar = strs.pop(indexOfMinLengthWord(strs))
    # 空文字が含まれていた場合は共通するprefixは絶対にないので空文字を返す
    if tar == "":
        return ""

    prefix = ""
    for c in tar:
        # 探索するprefixを作成
        prefix += c
        for word in strs:
            if prefix != word[:len(prefix)]:
                # 探索するprefixが1文字の時で単語に含まれていない場合
                if len(prefix) == 1:
                    return ""
                # 前のループで見つかっていたprefixを返す
                return prefix[:-1]

    return prefix


# strs = ["flower","flow","flight"] -> fl
# strs = ["flower","flow",""] -> ""
# strs = ["dog","racecar","car"] -> ""
# strs = ["d"] -> "d"
# strs = ["ssssssss", "ssss", "sssdss"] -> "sss"
# strs = ["reflower", "flow", "flight"] -> ""
print(longestCommonPrefix(["ssssssss", "ssss", "sssdss"]))
