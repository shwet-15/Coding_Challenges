#We are given a list nums of integers representing a list compressed with run-length encoding.
#Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such pair, there are freq elements with value val concatenated in a sublist. Concatenate all the sublists from left to right to generate the decompressed list.
#Return the decompressed list.

def decompressRLElist(nums):
    freq=0
    val=0
    n=len(nums)//2
    l=[]
    for i in range(0,n):
        freq=nums[i*2]
        val=nums[i*2 + 1]
        for j in range(freq):
             l.append(val)
    return l
print(decompressRLElist([1,2,3,4]))   
print(decompressRLElist([1,1,2,3]))     