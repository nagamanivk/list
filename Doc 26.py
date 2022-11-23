# """26. Our task is to print the element which occurs 3 consecutive times in a Python list.
# Example:
# Input: [4, 5, 5, 5, 3, 8]
# Output: 5
# Input: [1, 1, 1, 64, 23, 64, 22, 22, 22]
# Output: 1, 22"""
# a=[4,5,5,5,3,8]
a=[1, 1, 1, 64, 23, 64, 22, 22, 22]
i=0
b=[]
t=[]
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
        c=a.count(a[i])
        if c==3:
            t.append(a[i])
    i=i+1
print(t)

    






# a=int(input('enter the number'))
# b=int(input('enter the number'))
# sum=0
# i=0
# while i<b:
#     sum+=a
#     i+=1
# print(sum)




    
    


