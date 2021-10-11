def removeElement(nums,val):
    for item in nums:
        if item == val:
            nums.remove(item)
    i=0
    while i<len(nums):
        return nums[i]
        i+=1

arr= [0,1,2,2,3,0,4,2]

print(removeElement(arr,2))
