# a=[1,2,3,2,1,2,1]
# i=0
# b=[]
# while i<len(a):
#     if a[i] not in b:
#         b.append(a[i])
#     i=i+1
# print(b)

# a=[1,2,4,2,7,1,4]
# i=0
# while i<len(a):
#     c=a.count(a[i])
#     if c==1:
#         print([a[i]])
#     i=i+1

# a="mani"
# i=0
# b=[]
# while i<len(a):
#     b.append(a[i])
#     i=i+1
# print(b)

# a=[1,2,3,4,5,6]
# i=0
# d=-1
# b=[]
# while i<len(a)/2:
#     b.append(a[d])
#     b.append(a[i])
#     i=i+1
#     d=d-1
# print(b)

# a=[1,1,2,3,4,5,1,2]
# i=0
# b=[]
# n=int(input("enter the no:"))
# while i<len(a):
#     if a[i]!=n:
#         b.append(a[i])
#     i=i+1
# print(b)

# a=[5,6,[],3,[],[],9]
# i=0
# b=[]
# while i<len(a):
#     if a[i]!=[]:
#         b.append(a[i])
#     i=i+1
# print(b)

# a=[2,-7,5,-64,-14]
# p_n=0
# n_n=0
# i=0
# while i<len(a):
#     if a[i]>0:
#         p_n+=1
#     else:
#         n_n+=1
#     i=i+1
# print(p_n)
# print(n_n)

# a=int(input("enter the no:"))
# while a<=5:
#     if a<0:
#         print(a,end="")
#     a=a+1
# a=int(input("enter the no:"))
# b=int(input("enter the no:"))
# while a<=b:
#     if a<0:
#         print(a,end="")
#     a=a+1

# a=[12,67,98,34]
# i=0
# b=[]
# while i<len(a):
#     sum=0
#     while a[i]>0:
#         r=a[i]%10
#         sum=sum+r
#         a[i]=a[i]//10
#     b.append(sum)
#     i=i+1
# print(b)

# a=[34.7,12,-94.8,"dubbi",0,"mani"]
# i=0
# b=[]
# while i<len(a):
#     if type (a[i]) is int:
#         b.append(a[i])
#     i+=1
# print(b)

# a=[1,2,3,4,5,6]
# i=0
# b=[]
# while i<len(a)-1:
#     d=[a[i],a[i+1]]
#     b.append(d)
#     i=i+1
# print(b)

# a=[1,3,7,9,11,0,2,4,6,8,10,8,9,0,4,3,0]
# a=['s', 'd', 'f', 'j', 's', 'a', 'j', 'd', 'f', 'd']
# i=3
# j="z"
# while i<len(a):
#     a.insert(i,j)
#     i=i+4
# print(a)
# a=['s', 'd', 'f', 'j', 's', 'a', 'j', 'd', 'f', 'd']
# i=3
# while i<len(a):
#     a.insert(i,"z")
#     i=i+4
# print(a)

# a=[3,8,9,4,5,0,5,0,3]
# i=0
# b=[]
# while i<len(a):
#     b.append(a[i]+3)
#     i=i+1
# print(b)

# a=[1,2,3,4,5,45,67,78,89,90,34,5,]
# i=0
# b=[]
# n=int(input("enter the no:"))
# while i<len(a)-n:
#     b.append(a[i])
#     i=i+1
# print(b)

# a=[[1,2],[2,4]]
# i=0
# c=[]
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         d=a[j]
#         j=j+1
#     c.append(j)
#     i=i+1
# print(c)
    
# a=["red","maroon","yellow","alive"]
# i=0
# b=[]
# while i<len(a):
#     c=list(a[i])
#     b.append(c)
#     i=i+1
# print(b)

# a=[12,45,23,67,78,90,45,32,100,76,38,62,73,29,83]
# i=0
# b=[]
# while i<len(a):
#     d=[a[i],a[i+1],a[i+2]]
#     b.append(d)
#     i=i+3
# print(b)

# a=[2,0,4,00,130]
# # o/p:[2,4,1,3,0000]
# i=0
# j=0
# b=[]
# c=[]
# while i<len(a):
#     d=a[i]
#     if d>=a[j] and d!=0:
#         b.append(d)
#     elif d==0:
#         c.append(d)
#     i=i+1
#     j=j+1
# c.extend(d)
# print(c)

# a="6myname9is2jyothi5"
# i=0
# b=[]
# while i<len(a):
#     d=a[i]
#     if d.isalpha():
#         b.append(d)
#     i=i+1
# p="".join(b)
# print(p)

# a="my name is mani"
# b=a.split()
# i=0
# while i<len(b):
#     d=b[i]
#     e=d.capitalize()
#     print(e,end="")
#     i=i+1

# a=[6,9]
# b=a[0]
# c=a[1]
# d=[]
# while b<=c:
#     d.append(b)
#     b=b+1
# print(d)

