"""For example, if we give 9119  the function should return  811181, as the  square of 9 is 81 and square of 1  is 1."""
# a=[9,1,1,9]
# b=[]
# i=0
# while i<len(a):
#     c=a[i]**2
#     b.append(c)
#     i=i+1
# print(b)

# a=[9,1,1,9]
# b=[]
# for i in a:
#     c=i**2
#     b.append(c)
#     i=i+1
# print(b)

a=[[0],[1,3],[5,7],[9,11],[13,15,17]]
i=0
max=a[i]
while i<len(a):
    if a[i]>max:
        max=a[i]
    i=i+1
print(len(max),max)
        


    