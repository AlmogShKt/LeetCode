def maxProduct(nums):
    result = max(nums)
    curMax, curMin = 1, 1

    for n in nums:
        if n == 0:
            curMax, curMin = 1, 1
            continue
        tempMax = curMax * n
        curMax = max(curMax * n, curMin * n, n)
        curMin = min(tempMax, curMin * n, n)
        result = max(curMax, result)

    return result


# -48
nums = [2, -3, -2, -4]
print(maxProduct(nums))
