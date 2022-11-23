# n=int(input("enter the no:"))
# a=n
# len=len(str(n))
# sum=0
# while n>0:
#     r=n%10
#     b=r**len
#     sum=sum+b
#     n=n//10
# if a==sum:
#     print("ams no")
# else:
#     print("not")

n=int(input("enter the no:"))
a=n
sum=0
len=len(str(n))
for i in range (0,n):
    r=n%10
    b=r**len
    sum=sum+b
    n=n//10
if a==sum:
    print("ams no")
else:
    print("not")