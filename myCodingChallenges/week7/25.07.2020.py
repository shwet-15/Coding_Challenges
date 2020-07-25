def findMin(nums) :
    l=list(set(nums))
    l.sort()
    return l[0]
print(findMin([5,2,4,8,2,5,1]))   