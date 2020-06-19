#Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.
#Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

def removeDuplicates(nums) :
        for i in nums:
            c=nums.count(i)
            if c>2:
                while(nums.count(i)>2):
                    nums.remove(i)
        return len(nums)  
print(removeDuplicates([1,1,1,2,2,3]))    
print(removeDuplicates([0,0,1,1,1,1,2,3,3]) )                  