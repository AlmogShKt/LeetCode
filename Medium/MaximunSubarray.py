# 53. Maximum Subarray
def maxSubArray(nums) -> int:
    max_sum = nums[0]
    curSum = max_sum

    for i in range(1, len(nums)):
        curSum = max(curSum + nums[i], nums[i])
        max_sum = max(curSum, max_sum)

    return max_sum


nums = [5, 4, -1, 7, 8]
# nums = [-3, -1, -2]
print(maxSubArray(nums))
