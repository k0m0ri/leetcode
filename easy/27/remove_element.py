# def swap(nums, i, j):
#     tmp = nums[i]
#     nums[i] = nums[j]
#     nums[j] = tmp

# def remove_element(nums: [int], val: int) -> int:
#     non_val_last = 0
#     runner = 0

#     while runner < len(nums):
#         if not nums[runner] == val:
#             swap(nums, non_val_last, runner)
#             non_val_last += 1
#         runner += 1
#     return non_val_last


def remove_element(nums: [int], val: int) -> int:
    nums_len = len(nums)
    if nums_len == 0:
        return 0

    k = 0
    for _ in range(nums_len):
        if nums[k] == val:
            del nums[k]
        else:
            k += 1

    return k


# test
nums = [3, 2, 2, 3]
val = 3
k = remove_element(nums, val)

for i in range(k):
    print(nums[i])
