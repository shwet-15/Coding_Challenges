# 9. Write a function sumPdivisors() that finds the sum of proper divisors of a number. Proper
#     divisors of a number are those numbers by which the number is divisible, except the
#     number itself. For example proper divisors of 36 are 1, 2, 3, 4, 6, 9, 12, 18


def sumPdivisors(number):
    sum=1
    for i in range(2,number):
        if(number%i==0):
            sum=sum+i
    return sum   
n=int(input("Enter the number : "))

print("The sum of proper divisors of {} is {}".format(n,sumPdivisors(n)))