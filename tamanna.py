# a=["Tamanna","is","tanwar"]
# i=0
# b=[]
# while i<len(a):
#     d=a[i]
#     i+=1
#     print(d," ",end="")

# a=1234
# i=0
# s=0
# while a>0:
#     r=a%10
#     b=s+r
#     a=a//10
#     i+=1
#     print(b,end="")
# b=[]
# a=[2,3,[1,2,[3,4,6,9],14,13]]
# b.append(a[2][1])
# b.append(a[2][2][2])
# b.append(a[2][4])
# print(b)
# b=[]
# a=[2,3,[1,2,[4,5],[6,9],6,9],5,9]
# b.append(a[2][1])
# b.append(a[2][3][1])
# b.append(a[2][5])
# b.append(a[4])
# print(b)

# a=[1,2,[4,5,6]]
# b=[]
# i=0
# sum=0
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         s=0
#         while j<len(a):
#             s+=a[i][j]
#             j+=1
#         b.append(s)
#     else:
#         sum+=a[i]
#     i+=1
# b.append(sum)
# print(b)





# a=[2,[4,5],6]
# i=0
# f=1
# while i<len(a):
#     if type (a[i])==list:
#         j=0
#         while j<len(a[i]):
#             f=f*a[i][j]
#             j=j+1    
#     else:
#         f=f*a[i]
#     i+=1
# print(f)

# a=[2,[4,5],6]
# i=0
# b=[]
# while i<len(a):
#     if type (a[i])==list:
#         j=0
#         while j<len(a[i]):
#             b.append(a[i][j])
#             j+=1
#     else:
#         b.append(a[i])
#     i+=1
# print(b)
        

# a=[2,[4,5],6]
# i=0
# sum=0
# while i<len(a):
#     if type (a[i])==list:
#         j=0
#         while j<len(a[i]):
#             sum=sum+a[i][j]
#             j+=1
#     else:
#         sum=sum+a[i]
#     i+=1
# print(sum)

# a=[1,2,3,4,[6,7,10],8,10,[7],6,90]
# i=0
# max=a[0]
# while i<len(a):
#     if type (a[i])==list:
#         j=0
#         while j<len(a[i]):
#             if a[i][j]>max:
#                 max=a[i][j]
#             j+=1
#     elif a[i]>max:
#         max=a[i]
#     i=i+1
# print(max)

# a=[1,2,3,4,[6,7,0,10],8,10,[7],6,90]
# i=0
# max=a[0]
# min=a[0]
# while i<len(a):
#     if type (a[i])==list:
#         j=0
#         while j<len(a[i]):
#             if a[i][j]>max:
#                 max=a[i][j]
#             elif a[i][j]<min:
#                 min=a[i][j]
#             j+=1
#     elif a[i]>max:
#         max=a[i]
#     elif a[i]<min:
#         min=a[i]
#     i=i+1
# print(max)
# print(min)



# a=[[1,2,3],[5,6,7],[4,3,1]]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     sum=0
#     while j<len(a[i]):
#         sum=sum+a[j][i]
#         j+=1
#     b.append(sum)
#     i+=1
# print(b)

# a=[5,6,7,8,9]
# i=0
# c=1
# b=[]
# while i<len(a):
#     d=str(a[i]+c)
#     if len(d)>1:
#         e=a[1]
#         f=int(e)
#         b.append(f)
#     else:
#         r=int(d)
#         b.append(r)
#     i+=1
#     c+=1
# print(b)


# a=[5,6,7,[8,9,[56,78],[9,1,3]]]
# i=0
# sum=0
# while i<len(a):
#     if type (a[i])==list:
#         j=0
#         while j<len(a[i]):
#             if type (a[i][j]) is list:
#                 k=0
#                 while k<len(a[i][j]):
#                     sum=sum+a[i][j][k]
#                     k+=1
#             else:
#                 sum=sum+a[i][j]
#             j+=1
#     else:
#         sum=sum+a[i]
#     i+=1
# print(sum)

# a=[1,2,3,4,5,6]
# i=0
# sum=0
# c=0
# while i<len(a):
#     sum=sum+a[i]
#     i+=1
# d=sum/i
# print(d)

# a=[-1,4,5,-6,2,4]
# i=0
# p_n=0
# n_n=0
# b=[]
# c=[]
# while i<len(a):
#     if a[i]>0:
#         p_n+=1
#         b.append(a[i])
#     else:
#         n_n+=1
#         c.append(a[i])
#     i+=1
# print(b)
# print(c)

# a=[12,14,0,1,2,3]
# i=0
# e=0
# o=0
# while i<len(a):
#     if a[i]%2==0:
#         e+=1
#     else:
#         o+=1
#     i+=1
# print(e)
# print(o)


# a=[12,236,248,123]
# i=0
# b=[]
# while i<len(a):
#     sum=0
#     while a[i]>0:
#         sum+=a[i]%10
#         a[i]=a[i]//10
#     i+=1
#     b.append(sum)
# print(b)

# a=[1,2,[4,5],[6,7],8,9] 
# b=[]   
# b.append(a[1])
# b.append(a[2][1])
# b.append(a[3][1])
# b.append(a[5])  
# print(b)

# a=[2,4,[5,4,3],6,4]
# sum=0
# i=0
# while i<len(a):
#     if type (a[i])==list:
#         j=0
#         while j<len(a[i]):
#             sum=sum+a[i][j]
#             j+=1
#     else:
#         sum=sum+a[i]
#     i+=1
# print(sum)

a=["nagamani","Chaitu","Jyothi"]
i=0
n=input("enter the letter:")
while i<len(a):
    if a[i][0]==n:
        print(a[i])
    i+=1




# a="1234"




# a="1234abcd"
# i=1
# b=[]
# while i<=len(a):
#     d=a[-i]
#     b.append(d)
#     i+=1
# print(b)


# a="1234"
# i=-1
# b=[]
# while i>=-len(a):
#     c=a[i]
#     b.append(c)
#     i-=1
# print(b)

# a=[-1,4,5,-6,2,4]
# i=0
# p_n=0
# n_n=0
# b=[]
# c=[]
# while i<len(a):
#     if a[i]>0:
#         p_n+=1
#         b.append(a[i])
#     else:
#         n_n+=1
#         c.append(a[i])
#     i+=1
# print(b)
# print(c)




    

        
    



    













    
    


            


        
        
        
    
        
        




        

            



    




