# https://leetcode.com/problems/roman-to-integer/description/
#3 17-5-53


def romanToInt(s: str) -> int:
    symbol_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    sum = 0
    for i in range(len(s) - 1):
        j = i + 1
        if symbol_map[s[i]] < symbol_map[s[j]]:
            sum -= symbol_map[s[i]]
        else:
            sum += symbol_map[s[i]]

    return sum + symbol_map[s[-1]]

s = "MCMXCIV"
print(romanToInt(s))

