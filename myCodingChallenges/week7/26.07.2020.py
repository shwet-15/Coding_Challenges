#Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.



def singleNumber(nums):
        nums.sort()
        for i in range(0,len(nums)-2,3):
            if nums[i]==nums[i+1] and nums[i]==nums[i+2]:
                continue
            else:
                return(nums[i])
                break 
        else:
            return(nums[-1]) 
print(singleNumber([0,1,0,1,0,1,99]))