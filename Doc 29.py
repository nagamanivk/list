"""Remove empty List from List		
The original list is: [5, 6, [], 3, [], [], 9]
List after empty list remova"""




a=[5,6,[],3,[],[],9]
i=0
b=[]
while i<len(a):
    if a[i]!=[]:
        b.append(a[i])
    i=i+1
print(b)

    


