"""4. List product excluding duplicates.
	List = [6,1,3,5,6,3,1]
	Output: 60"""

a=[6,1,3,5,6,3,1]
b=[]
i=0
p=1
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
        p=p*a[i]
    i=i+1
print(p)
