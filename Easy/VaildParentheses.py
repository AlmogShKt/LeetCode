def isValid(s: str) -> bool:
    def_count = 0
    parentheses_types = {
        "(": 0,
        ")": 0,
        "{": 0,
        "}": 0,
        "[": 0,
        "]": 0,
    }

    for c in s:
        if c in "({[":
            if parentheses_types[c] >= 0:
                parentheses_types[c] += 1
            else:
                return False
        else:
            parentheses_types[c.replace(")", "(").replace("}", "{").replace("]", "[")] -= 1
    for key in parentheses_types:
        if parentheses_types[key] != 0:
            return False

    return True



s = "([)]"
print(isValid(s))