# 739. Daily Temperatures
def dailyTemperatures(temperatures):
    result = [0] * len(temperatures)
    stack = []  # paits of temp index in array

    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            stackT, stackI = stack.pop()
            result[stackI] = i - stackI
        stack.append((t, i))

    return result


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(dailyTemperatures(temperatures))
