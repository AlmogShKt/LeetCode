import collections
#387. First Unique Character in a String
def firstUniqChar(s):
    letters_diagram = collections.defaultdict(int)
    for c in s:
        letters_diagram[c] += 1

    for i, c in enumerate(s):
        if letters_diagram[c] == 1:
            return i
    return -1

