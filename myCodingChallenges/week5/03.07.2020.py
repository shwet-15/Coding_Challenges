#Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.
#The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.

def findTheDistanceValue(arr1, arr2, d):
        c=0
        for i in range(len(arr1)):
            for j in range(len(arr2)):
                if abs(arr1[i]-arr2[j]) <=d:
                    break
            else: 
                c=c+1
        return c
print(findTheDistanceValue(arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2))
print(findTheDistanceValue(arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3))
print(findTheDistanceValue(arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6))

        