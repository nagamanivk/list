"""Write a Python program to pair up the consecutive elements of a given list.
Original lists:
[1, 2, 3, 4, 5, 6]
Pair up the consecutive elements of the said list:
[[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]"""

a=[1, 2, 3, 4, 5, 6]
i=0
b=[]
while i<len(a)-1:
    d=a[i],a[i+1]
    b.append(d)
    i=i+1
print(b)
