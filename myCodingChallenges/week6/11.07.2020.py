#Given an array of unique integers salary where salary[i] is the salary of the employee i.
#Return the average salary of employees excluding the minimum and maximum salary.

def average(salary):
  salary.sort()
  s=0
  for i in range(1,len(salary)-1):
     s=  s + salary[i]
  return(s/(len(salary)-2)) 
print(average([6000,5000,4000,3000,2000,1000]))
print(average([8000,9000,2000,3000,6000,1000]))