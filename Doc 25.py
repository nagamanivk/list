"""25. Given a List, extract all elements whose frequency is greater than K.
Input: test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8], K = 3
Output: [4, 3]
Explanation: Both elements occur 4 times.
Input: test_list = [4, 6, 4, 3, 3, 4, 3, 4, 6, 6], K = 2
Output: [4, 3, 6]
Explanation: Occur 4, 3, and 3 times respe"""
l=[4,6,4,3,3,4,3,4,3,8]
i=0
b=[]
k=3
t=[]
while i<len(l):
    if l[i] not in b:
        b.append(l[i])
        c=l.count(l[i])
        if c>k:
            t.append(l[i])
    i=i+1
print(t)
    


    
