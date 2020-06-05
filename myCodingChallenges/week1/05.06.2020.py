def twoSum(nums, target) :
  l=[]
  for i in range(0,len(nums)):
      for j in range(1,len(nums)):
          if nums[i]+nums[j]==target and i!=j:
              l.append(i)
              l.append(j)
              return l
print(twoSum([5,8,3,9,30,10],40))