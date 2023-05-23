#two inputs followed by an array, one is total no. of element, 2nd is target array, find the no. of elements in the array
#having sum as target value
#it should be the array with maximum numbers

n = 4
trg = 10
arr = [3,2,5,5]
arr_max = []
for i in range(n):
    for j in range(n+1):
        temp = arr[i:j]
        if(sum(temp)==trg):
            arr_max.append(len(temp))
print(max(arr_max))
