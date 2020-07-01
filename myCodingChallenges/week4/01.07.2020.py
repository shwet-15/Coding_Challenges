#Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
    
def maxProduct(nums) :
        n1=max(nums)
        n1_i=nums.index(n1)
        nums.pop(n1_i)
        n2=max(nums)
        result=(n1-1)*(n2-1)
        return(result)
print(maxProduct([3,4,5,2]))
print(maxProduct([1,5,4,5]))
print(maxProduct([3,7]))

    
        