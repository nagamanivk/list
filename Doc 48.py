"""Write a Python program to split a given list into specified sized chunks. 
Original list:
[12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
Split the said list into equal size 3
[[12, 45, 23], [67, 78, 90], [45, 32, 100], [76, 38, 62], [73, 29, 83]]
Split the said list into equal size 4
[[12, 45, 23, 67], [78, 90, 45, 32], [100, 76, 38, 62], [73, 29, 83]]
Split the said list into equal size 5
[[12, 45, 23, 67, 78], [90, 45, 32, 100, 76], [38, 62, 73, 29, 83]]"""
a=[12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
i=0
b=[]
while i<len(a):
    d=[a[i],a[i+1],a[i+2]]
    b.append(d)
    i=i+3
print(b)


    

