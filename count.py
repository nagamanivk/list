# i=["mani","jyothi","jyothi","jyothi","jyothi"]
# print(i.count("jyothi"))

# i=1
# even_sum=0
# odd_sum=0
# c1=0
# c2=0
# while i<=10:
#     if i%2==0:
#         even_sum=even_sum+i
#         c1+=1
#     else:
#         odd_sum=odd_sum+i
#         c2+=1
#     i+=1
# print("even_sum:", even_sum%c1)
# print("odd_even:",odd_sum%c2)


a=[1,2,3,1,2,2]
b=[]
i=0
while i<len(a):
    if a[i]!=a[i+1]:
        b.append(a[i])
    i+=1
print(b)