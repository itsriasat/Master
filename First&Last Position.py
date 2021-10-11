nums = [5,7,7,7,7,10]
target = 8
Output: [3,4]


def FirstBinarySearch(arr,low,high,target):
    while low<=high:
        mid = low +  (high-low)// 2
        if arr[mid]==target and arr[mid-1]!=target:
            return mid
        elif arr[mid]>target:
            high = mid-1
        elif arr[mid]<target:
            low=mid+1
        else:
            low = low-1
    return -1

def LastBinarySearch(arr,low,high,target):
    index = -1
    while low<=high:
        mid = low +  (high-low)// 2
        if arr[mid]>=target:
            high = mid-1
        else:
            low=mid+1
        if arr[mid] == target:
            index =mid
    return index

def SearchRange(nums,target):
    first_position = FirstBinarySearch(nums,0,len(nums)-1,target)
    last_position = LastBinarySearch(nums,first_position,len(nums)-1,target)
    return first_position,last_position

print(SearchRange(nums,8))