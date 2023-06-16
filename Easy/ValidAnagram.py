# 242. Valid Anagram

def isAnagram(s: str, t: str) -> bool:
    s_list = list(s)
    s_list.sort()
    t_list = list(t)
    t_list.sort()
    if s_list == t_list:
        return True
    return False


def isAnagram2(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    for key in countS.keys():
        if countT.get(key, 0) != countS[key]:
            return False
    return True
