
#T - no. of test cases
# n = no. in sequence
# seq = sequence
T = int(input())


for i in range(T):
    k = []
    flag = 0
    n = int(input())
    seq = map(int, input().split())
    count_dict = {}
    for i in seq:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict.update({i : 1})
    k = list(count_dict.values())
    recommend = max(count_dict,key = count_dict.get)
    if(k.count(count_dict[recommend]) > 1):
        print('Confused')
    else:
        print(recommend)