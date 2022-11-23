# n=int(input("enter the number"))
# a=n%1000
# c=a%100
# d=c%10
# print(n-a,"+",a-c,"+",c-d,"+",d)

# n=int(input("enter the no:"))
# s=""
# i=0
# while i<=n:
# a=["a","b","c"]
# b="".join(a)
# print(b)

# a=["muktai","nani"]
# i=0
# while i<len(a)-1:
#     print(a[i][i],".",a[i+1][i])
#     i=i+1

# a="hello"
# i=-1
# b="h"
# while i>-len(a):
#     b=b+a[i]
#     i=i-1
# print(b)



# a=["jyo","mani"]                   # o/p"oyj","inam"
# i=0
# b=[]
# while i<len(a):
#     d=a[i]
#     j=d[::-1]
#     b.append(j)
#     i=i+1
# print(b)

a=["jyo","mani"]
i=0
b=[]
while i>-len(a):
    d=a[i]
    j=-1
    r=""
    while j>=-len(d):
        r=r+d[j]
        j=j-1
    i=i-1
    b.append(r)
print(b)

# a="chaitanya"
# b=list(a)
# print(b)

    

