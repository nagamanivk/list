"""Given start and end of a range, write a Python program to print all positive numbers in given range.
Example:
Input: start = -4, end = 5
Output: 0, 1, 2, 3, 4, 5 

Input: start = -3, end = 4
Output: 0, 1, 2, 3, 4"""


n=int(input("enter the no:"))
m=int(input("enter the no:"))
while n<=m:
    if n>=0:
        print(n,end=" ")
    n=n+1

