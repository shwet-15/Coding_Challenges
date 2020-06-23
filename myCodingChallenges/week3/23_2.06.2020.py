#Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
#Return the array in the form [x1,y1,x2,y2,...,xn,yn].

def shuffle(nums,n):
    i=1
    while(n<len(nums)):
       temp=nums[n]
       nums.pop(n)
       nums.insert(i,temp)
       n=n+1
       i=i+2
    return nums
print(shuffle([2,5,1,3,4,7],3))
print(shuffle([1,1,2,2], 2))
print(shuffle([1,2,3,4,4,3,2,1],4))
