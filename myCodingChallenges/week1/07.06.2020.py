# 1. Write a function that inputs a number and prints the multiplication table of that number
def multiplication_table(n):
    for i in range(1,11):
        product=n*i
        print("{} * {} = {}".format(i,n,product))
number=int(input("Enter the number : "))        
print("Multiplication table of {}".format(number))
multiplication_table(number) 