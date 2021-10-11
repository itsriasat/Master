nums = [100,4,200,1,3,2]
nums_2 = [0,3,7,2,5,8,4,6,0,1]
nums_3=[1,3,5]

def FindLongestSequence(nums):
    if len(nums)==0:
        return -1
    if len(nums)==1:
        return 1
    nums.sort()
    count=1
    result = []
    for i in range(0,len(nums)-1):
        if nums[i+1]-nums[i]==1 or nums[i+1]==nums[i]:
            if nums[i]==0 and nums[i+1]==0:
                pass
            else:
                count+=1
        else:
            result.append(count)
            count = 1
    result.append(count)
    return max(result)
print(FindLongestSequence(nums_3))


