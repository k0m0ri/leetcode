# 別解　標準ライブラリを使用した方がシンプルに記載できるし速い
# def removeDuplicates(nums: list[int]) -> int:
#     nums[:] = sorted(set(nums))
#     return len(nums)


def removeDuplicates(nums: list[int]) -> int:
    nums_len = len(nums)
    if nums_len == 1:
        return 1

    k = 1
    pre = nums[0]
    for num in range(1, nums_len):
        cur = nums[k]
        if cur != pre:
            pre = cur
            # popする位置を進める
            k += 1
        else:
            del nums[k]

    return k


# test
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 6, 6, 8]
k = removeDuplicates(nums)
for i in range(k):
    print(nums[i])
