#Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.
#For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the greatest number of candies among them. Notice that multiple kids can have the greatest number of candies.

def kidsWithCandies(candies, extraCandies):
   m=max(candies)
   l=[]
   for i in candies:
      if i+extraCandies>=m:
          l.append(True)
      else:
          l.append(False)
   return l
print(kidsWithCandies([12,1,12],10))  
print(kidsWithCandies([4,2,1,1,2],1)) 
print(kidsWithCandies([2,3,5,1,3],3))  


