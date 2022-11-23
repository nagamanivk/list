# a=[1,2,3,4]
# b="emp"
# i=0
# c=[]
# while i<len(a):
#     d=b+str(a[i])
#     c.append(d)
#     i=i+1
# print(c)




from binascii import a2b_hex


# a=[[1,2,3],[4,5,6],[7,8,9]]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     s=0
#     while j<len(a):
#         s=s+a[i][j]
#         j=j+1
#     i=i+1
#     b.append(s)
# print(b)




a=[[1,2,3],[1,2,3],[1,2,3]]
i=0
b=[]
while i<len(a):
    j=0
    s=0
    while j<len(a):
        s=s+a[i][j]
        j=j+1
    i=i+1
    b.append(s)
print(b)


