
#create reverse of a string without affecting special characters

s = "a!!!b.c.d,e'f,ghi"
k = ""
m = ""

#making a separate string "k" which will contain all alphas of string s
# in k : replacing special characters with ' '
for i in s:
    if i.isalpha():
        k += i
    else:
        k += ' '
l = k.replace(' ','')
#creating reverse of string without special characters
l = l[::-1]
x=0

#replacing all spaces in k with the special characters of s
for i in range(len(k)):
    if(k[i] == ' '):
        m += s[i]
    else:
        m += l[x]
        x += 1

#printing
print(m)