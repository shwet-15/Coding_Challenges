#Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
#The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

def twoSum( numbers,target):
    l=0
    h=len(numbers)-1
    while(l<h):
        if(numbers[l] +numbers[h]<target):
            l=l+1
        elif(numbers[l] +numbers[h]>target): 
            h=h-1
        elif(numbers[l] +numbers[h]==target):
            return(l+1,h+1)
print(twoSum([2,7,11,15],9))        
           