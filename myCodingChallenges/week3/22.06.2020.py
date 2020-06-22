#Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
#Find all the elements of [1, n] inclusive that do not appear in this array.

def findDisappearedNumbers(nums):
    n=set(nums)
    li=[]
    for i in range(1,len(nums)+1):
        if i not in n:
           li.append(i)      
    return li   
print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))

