
def findDisappearedNumbers(nums):
    nums.sort()
    result = []

    for i in range(0, len(nums)-1):
        if nums[i+1]-nums[i]>1:
            diff = nums[i+1]-nums[i]-1
            x=1
            while x<=diff:
                result.append(nums[i]+x)
                x+=1
    return result

nums = [4,3,2,7,8,2,3,1]
print(findDisappearedNumbers(nums))