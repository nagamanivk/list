# """14. Write a Python program to find the list with maximum and minimum length.
# Original list:
# [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# List with maximum length of lists:
# (3, [13, 15, 17])
# List with minimum length of lists:
# (1, [0])"""

l=[[0],[1,3],[5,7],[9,11],[13,15,17]]
i=0
max=l[i]
min=l[i]
while i<len(l):
    if l[i]>max:
        max=l[i]
    elif l[i]<min:
        min=l[i]
    i=i+1
print((len(max),max))
print((len(min),min))
        

    


