def InsertPosition(nums,target):
    low,high=0,len(nums)-1
    index= -1
    while low<=high:
        mid = low +  (high-low)// 2
        if nums[mid]==target:
            index= mid
            high=mid-1
        elif nums[mid]>target:
            high = mid-1
        else:
            low=mid+1
    if index>-1:
        return index
    else:
        return high+1
nums = [1,2,2,2,2,3,4,5,6,7,8]
print(InsertPosition(nums,2))