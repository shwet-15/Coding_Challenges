#Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#You may assume no duplicates in the array.

def searchInsert( nums, target):
  high=len(nums)-1
  low=0
  Found=False
  while(low<=high):
    mid=(low+high)//2
    if target==nums[mid]:
       Found=True
       return mid
    elif target<nums[mid]:
      high=mid-1
    elif target>nums[mid]:
      low=mid+1
  if Found==False:
      for i in nums:
        if len(nums)==1 and target<i:
          return 0
      for i in range(0,len(nums)-1):
         if target<nums[i]:
           return 0
         if target>nums[i] and target<nums[i+1]:
            nums.insert(i+1,target)
            return i+1
      else:
        return len(nums)
r=searchInsert([1,3,5,8],7)
s=searchInsert([1,3,5,8],3)
print(r) 
print(s) 



