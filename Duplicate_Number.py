def findDuplicate(nums):
    s=sorted(nums)
    for i in range(0,len(s)):
        if s[i]==s[i+1]:
            return s[i]
print(findDuplicate([1,3,4,2,2]))
    