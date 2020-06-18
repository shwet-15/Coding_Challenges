#There are two sorted arrays nums1 and nums2 of size m and n respectively.
#Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#You may assume nums1 and nums2 cannot be both empty.

def findMedianSortedArrays(nums1, nums2):
  nums1.extend(nums2)
  nums1.sort()
  l=0
  h=len(nums1)-1
  m=l+h//2
  if len(nums1)%2!=0:
    median=nums1[m]
    return median
  elif len(nums1)%2==0:
   median=(nums1[m]+nums1[m+1])/2
   return median

nums1 = [1, 3,6]
nums2 = [2,3,4]
print(findMedianSortedArrays(nums1, nums2)) 





