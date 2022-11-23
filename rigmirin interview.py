



        
# a=[1,2,3,5,7,6,9,8]
# i=0
# b=[]
# while i<len(a):
#           j=1
#           while j<len(a):
#                     if a[i]+a[j]==8:
#                               r=a[i],a[j]
#                               v=list(r)
#                               if v not in b:
#                                         b.append(v)
                              
#                     j=j+1
#           i=i+1
# print(b)

# a=[1,2,3,4,5,6,7,8]
# i=0
# while i<len(a)-6:
#     j=0
#     while j<len(a):
#         if a[i]+a[j]==8:
#             if a[i]<3:
#                 b=[a[i],a[j]]
#         j=j+1
#     i=i+1
#     print(b,end="")


# i=int(input("enter the number: "))
# i=0
# while i<=100:
#     i=i+1
#     if i%3==0 and i%5==0:
#         print("fizz buzz")
    
#     elif i%3==0:
#         print("fizz")
    
#     elif i%5==0:
#         print("buzz")
    
#     else:
#         print(i)



# a=input("enter the no:")
# if a.isupper():
#     print("true")
# elif a.islower():
#     print("false")
# elif a.isupper():
#     print("false")
# elif a.isdigit():
#     print("true")
# else:
#     print("true")

n=int(input("enter the no:"))
count=0
i=1
while i<=n:
    if n%i==0:
        count+=1
    i=i+1
if count==2:
    j=0
    sum=0
    while n>0:
        r=n%10
        sum=sum*10+r
        n=n//10
    count1=0
    k=1
    while k<=sum:
        if sum%k==0:
            count1+=1
        k=k+1
    if count1==2:
        print("twisted prime number")
    else:
        print("not a twisted prime number")
else:
    print("umber")