def longestCommonPrefix(strs):
    result = ""
    for i in range(len(strs[0])):
        for s in strs:
            if i == len(strs[0]) or s[i] != strs[0][i]:
                return result
        result += strs[0][i]

    return result


strs = ["almog","almogflow","almoflight"]

print(longestCommonPrefix(strs))