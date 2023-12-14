import sys

MAX = 10000
input = sys.stdin.readline
arr = [False, False, True] + [True, False] * 4999

for i in range(3, int(MAX**.5)+1, 2):
    if arr[i]:
        arr[i*i::2*i] = [False]*len(arr[i*i::2*i])

a = int(input())

for i in range(a):
    cmp_num = int(input())
    st = cmp_num //2
    
    if st == 2:
        print(st, st) 
         
    if st%2 == 0:
        st -= 1
    
    for j in range(st, 0, -2):
        added = cmp_num - j
        if arr[j] == True and arr[added]:
            print(j, added)
            break
        
