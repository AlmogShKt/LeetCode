# https://leetcode.com/problems/two-sum/description/

#1 - 17-5-23

def twoSum(nums, target):
    n = len(nums)
    dif = 0
    hashmap = {}
    for i, num in enumerate(nums):
        hashmap[num] = i

    for i in range(n):
        dif = target - nums[i]
        if dif in hashmap and hashmap[dif] != i:
            result = [i, hashmap[dif]]
    if result:
        return result
    else:
        return []

nums = [2,7,11,15]
target = 9
print(twoSum(nums,target))
