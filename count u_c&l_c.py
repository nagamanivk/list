a="PytHoNLANguage"
i=0
upper_c=0
lower_c=0
while i<len(a):
    if a[i].isupper():
        upper_c+=1
    else:
        lower_c+=1
    i=i+1
print("capital lettre count is:",upper_c)
print("capital lettre count is:",lower_c)
    