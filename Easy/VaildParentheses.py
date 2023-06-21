# 23-05-23
def isValid(s: str) -> bool:
    prent_stack = []
    open_pre = ["(", "{", "["]
    close_pre = [")", "}", "]"]
    if len(s) == 1:
        return False
    for p in s:
        if p in open_pre:
            prent_stack.append(p)
        if p in close_pre:
            try:
                temp_pre = prent_stack.pop()
            except IndexError:
                return False
            if not p.replace(")", "(").replace("}", "{").replace("]", "[") == temp_pre:
                return False

    if len(prent_stack) != 0:
        return False
    return True


s = "){"
print(isValid(s))


# second attempt:
def isValid2(s: str) -> bool:
    if len(s) == 1:
        return False

    valid_pairs = {
        "(": ")",
        "{": "}",
        "[": "]"}
    stack = []

    for p in s:
        if p in valid_pairs.keys():
            stack.append(valid_pairs[p])
        elif stack and p == stack[-1]:
            stack.pop()
        else:
            return False

    if len(stack) != 0:
        return False
    return True
