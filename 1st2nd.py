nums = [1,2,3]
def searchRange(nums, target) :
    if len(nums)==0:
        return -1 ,-1
    def FirstBinarySearch(arr ,low ,high ,target):
        index = -1
        while low<=high:
            mid = low +  (high -low )// 2
            if arr[mid]>=target:
                high = mid -1
            else:
                low =mid +1
            if arr[mid]==target:
                index = mid
        return index

    def LastBinarySearch(arr ,low ,high ,target):
        index = -1
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1
            if arr[mid] == target:
                index = mid
        return index

    first_position = FirstBinarySearch(nums ,0 ,len(nums ) -1 ,target)
    last_position = LastBinarySearch(nums ,first_position ,len(nums ) -1 ,target)
    return first_position ,last_position

print(searchRange(nums,2))

import jovian
jovian.commit()