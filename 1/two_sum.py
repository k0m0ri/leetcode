def twoSum(nums: [int], target: int) -> [int]:
    for i in range(0, len(nums) - 1):
        for j in range(i + 1, len(nums)):
            ans = nums[i] + nums[j]
            if ans == target:
                return [i, j]


# nums = [2, 7, 11, 15], target = 9
# nums = [3, 2, 4], target = 6
# nums = [3, 3], target = 6
nums = [3, 3]
target = 6
print(twoSum(nums, target))
