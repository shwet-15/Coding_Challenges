#Given two arrays of integers nums and index. Your task is to create target array under the following rules:
##Initially target array is empty.
#From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
#Repeat the previous step until there are no elements to read in nums and index.
#Return the target array.

def createTargetArray(nums,index):
    target=[]
    j=0
    for i in range(len(index)):
        target.insert(index[i],nums[j])
        j=j+1
    return target
print(createTargetArray([0,1,2,3,4],[0,1,2,2,1])) 
print(createTargetArray([1,2,3,4,0],[0,1,2,3,0]))  

