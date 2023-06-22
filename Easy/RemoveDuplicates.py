def removeDuplicates(nums):
    if len(nums) <= 1:
        return len(nums)
    n = len(nums)
    count_duplicates = 0
    left, right = 0, 1

    while right != n:
        if nums[left] == nums[right]:
            nums[right] = 101
            count_duplicates += 1
        else:
            left = right
        right += 1

    #nums.sort()
    print(nums)
    return n - count_duplicates


nums = [1,1,2]
print(removeDuplicates(nums))
