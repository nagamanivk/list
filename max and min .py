l=[4,5,6,78,56,76,56,89,3]
i=0
min=1000
max=0
while i<len(l):
    if l[i]>max: 
        max=l[i]
    elif l[i]<min:
        min=l[i]
    i=i+1
print(max)
print(min)

