
"""16. Write a Python program to find the difference between elements (n+1th - nth) of a given list of numeric values.
Original list:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Difference between elements (n+1th - nth) of the said list :
[1, 1, 1, 1, 1, 1, 1, 1, 1]
Original list:
[2, 4, 6, 8]
Difference between elements (n+1th - nth) of the said list :
[2, 2, 2]"""

l=[1,2,3,4,5,6,7,8,9,10]
b=[]
i=0
while i<len(l)-1:
    j=l[i+1]-l[i]
    b.append(j)
    i=i+1
print(b,end="")


    