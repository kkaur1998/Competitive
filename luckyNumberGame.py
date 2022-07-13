# cook your dish here
n = int(input())
for i in range(n):
    N,a,b = map(lambda x: int(x),input().split())
    seq1 = list(map(lambda x: int(x),input().split()))
    bob_count = 0
    alice_count = 0
    dummy = 0
    for i in seq1:
        if(i%a == 0 and i%b ==0):
            dummy += 1
        elif(i%a == 0):
            bob_count += 1
        elif(i%b == 0):
            alice_count += 1
    if(dummy > 0):
        bob_count += 1
    if(bob_count > alice_count):
        print('BOB')
    else:
        print('ALICE')





