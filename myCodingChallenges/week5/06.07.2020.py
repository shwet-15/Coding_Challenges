#Given a non-empty array of integers, every element appears twice except for one. Find that single one.

def singleNumber(nums):
    nums.sort()
    i=0
    while(i<len(nums)-1):
        if nums[i]==nums[i+1]:
            i=i+2
        else:
            break
    return nums[i]  
print(singleNumber([4,7,1,5,7,4,1]))    
