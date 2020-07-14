#Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.

def uniqueOccurrences(arr):
        counts=[]
        for i in arr:
            c=arr.count(i)
            counts.append(c)
        d={arr[i]:counts[i] for i in range(len(arr))}
        values=[]
        for v in d.values():
            values.append(v)
        values.sort()
        for i in range(len(values)-1):
            if values[i]==values[i+1]:
                return(False)
                break
        else:    
            return(True)  
print(uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0])) 
print(uniqueOccurrences([1,2,3,6,6]))            
       