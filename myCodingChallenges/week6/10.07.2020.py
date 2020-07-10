#Given two integer arrays startTime and endTime and given an integer queryTime.
#The ith student started doing their homework at the time startTime[i] and finished it at time endTime[i].
#Return the number of students doing their homework at time queryTime. More formally, return the number of students where queryTime lays in the interval [startTime[i], endTime[i]] inclusive.

def busyStudent(startTime,endTime,queryTime):
   count=0
   i=0
   j=0
   while(i<len(startTime)):
      if startTime[i]<=queryTime and endTime[j]>=queryTime:
        count +=1
      i=i+1  
      j=j+1
   return(count)  
startTime = [9,8,7,6,5,4,3,2,1]
endTime = [10,10,10,10,10,10,10,10,10]
queryTime = 5
print(busyStudent(startTime,endTime,queryTime))