# 49. Group Anagrams

def group(strs):
    res = {}
    for s in strs:
        count = [0] * 26  # a---z
        for c in s:
            count[ord(c) - ord("a")] += 1
        key = tuple(count)
        res.setdefault(key, []).append(s)

    return res.values()
