s = "a!!!b.c.d,e'f,ghi"
k = ""
m = ""
for i in s:
    if i.isalpha():
        k += i
    else:
        k += ' '
l = k.replace(' ','')
l = l[::-1]
x=0
for i in range(len(k)):
    if(k[i] == ' '):
        m += s[i]
    else:
        m += l[x]
        x += 1
print(m)