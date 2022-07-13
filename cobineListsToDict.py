
# make a dictionary using two given lists l1 and l2
l1 = ['a','b','c','d','e']
l2 = [2, 3, 7, 8,1]
d1 = {}
if(len(l1) != len(l2)):
    print("not possible")
else:
    for i in range(len(l1)):
        d1.update({l1[i] : l2[i]})

print(d1)