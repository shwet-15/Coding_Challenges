#Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
#Return the running sum of nums.

def runningSum(nums):
    s=[]
    i=0
    sum=0
    while(i<len(nums)):
        sum=sum+nums[i]
        s.append(sum)
        i=i+1
    return s
print(runningSum([3,1,2,10,1]))    
print(runningSum([1,1,1,1,1]))    
print(runningSum([1,2,3,4]))    


