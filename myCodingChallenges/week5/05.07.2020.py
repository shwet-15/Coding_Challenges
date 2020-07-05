#Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements. 
#Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows
#a, b are from arr
#a < b
#b - a equals to the minimum absolute difference of any two elements in arr

def minimumAbsDifference(arr):
        arr.sort()
        min=abs(arr[0]-arr[1])
        output=[]
        for i in range(len(arr)-1):
            diff=abs(arr[i]-arr[i+1])
            if diff<min:
                min=diff
        for i in range(len(arr)-1):
            l=[]
            if abs(arr[i]-arr[i+1])==min:
                l.append(arr[i])
                l.append(arr[i+1])
                output.append(l)
        return(output)    
print(minimumAbsDifference([4,2,1,3]))  
print(minimumAbsDifference([1,3,6,10,15]))  
print(minimumAbsDifference([3,8,-10,23,19,-4,-14,27]))                 