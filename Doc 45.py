""" Write a Python program to remove the last N number of elements from a given list. 
Original lists:
[2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5]
Remove the last 3 elements from the said list:
[2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34]
Remove the last 5 elements from the said list:
[2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34]
Remove the last 1 element from the said list:
[2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3]"""

a=[2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3]

i=0
b=[]
n=int(input("enter the no:"))
while i<len(a)-n:
    b.append(a[i])
    i=i+1
print(b)




    
