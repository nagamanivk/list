"""different. 
Original list:
[[1, 2, 4], [2, 4, 4], [1, 2]]
Sum said lists with different lengths:
[4, 8, 8]
Original list:
[[1], [2, 4, 4], [1, 2], [4]]
Sum said lists with different lengths:
[8, 6, 4]"""

# a=[[1, 2, 4], [2, 4, 4], [1, 2]]
# a=[[1], [2, 4, 4], [1, 2], [4]]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     s=0
#     while j<len(a)-1:
#         s+=a[j][i]
#         j=j+1
#     b.append(s)
#     i=i+1
# print(b)


# a=[[1], [2, 4, 4], [1, 2], [4]]
# i=0
# b=[]
# sum=0
# while i<len(a):
#     sum+=a[i][0]
#     i+=1
# b.append(sum)
# print(b)



a=[[1], [2, 4, 4], [1, 2], [4]]
i=0
b=[]
while i<len(a)-1:
    j=0
    s=0
    while j<len(a)-1:
        s=s+a[j][0]
        j=j+1
    b.append(s)
    i=i+1
print(s)

