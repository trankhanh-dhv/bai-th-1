b=''
a=input('nhap chuoi:')
for i in a:
    if i.isdigit() :
        continue
    else:
        b+=i
print(b)
