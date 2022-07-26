n = int(input())
a,b,c = input().split()
perm_list= []
g = []
output = []

for i in range(n):
    n = c[i]
    g.append(n+c[:i]+c[i+1:])

for l in g:
    for i in range(3):
        n = l[i]
        new = n+l[:i]+l[i+1:]
        if (new not in perm_list):
            perm_list.append(new)
