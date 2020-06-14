# a non-empty array of digits representing a non-negative integer, plus one to the integer.
#The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
#You may assume the integer does not contain any leading zero, except the number 0 itself.


def plusOne(digits):
    digits=[str(i) for i in digits]
    digits=''.join(digits)
    digits=int(digits)+ 1
    digits=[int(j) for j in str(digits)]
    return digits
print(plusOne([9,9,9]))
print(plusOne([2,7,9,0]))