"""
Input: letters = ['a', 'b', 'c', 'd', 'd', 'e', 'e', 'e', 'f', 'g'], target = 'd'
Output: 3

"""

def char_at(arr, char):
    left,right = 0, len(arr)-1
    mid = left+right / 2
    while left <= right:
        if arr[mid] == char:
            return mid
        elif arr[left] < char:
            left = mid

        else:
            right = mid

        mid = right + left / 2
    return mid

arr =  ['a', 'b', 'c', 'd', 'd', 'e', 'e', 'e', 'f', 'g']
target = 'd'
print(char_at(arr,target))