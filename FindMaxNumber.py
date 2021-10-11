def FindMaxNumber(arr):
    if len(arr) == 0:
        return -1
    max_val = -1
    for i in range(0, len(arr)):
        if max_val <= arr[i]:
            max_val = arr[i]
    return max_val
nums_2 = [0,3,7,2,5,8,4,6,0,1]
nums_2.sort()
print(FindMaxNumber(nums_2))