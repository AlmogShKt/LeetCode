# https://leetcode.com/problems/palindrome-number/
# 2 15-5-23
def isPalindrome(self, x: int) -> bool:
    x_str = str(x)
    i = 0
    j = len(x_str) - 1
    not_found = 1
    while (i <= j):
        if x_str[i] == x_str[j]:
            i += 1
            j -= 1
        else:
            return False
    return True

# With out converting


def isPalindrome(self, x: int) -> bool:
    if x < 0 or (x != 0 and x % 10 == 0):
        return False

    half = 0
    while x > half:
        half = (half * 10) + (x % 10)
        x = x // 10

    return x == half or x == half // 10
