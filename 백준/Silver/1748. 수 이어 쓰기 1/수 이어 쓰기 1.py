import sys

n = int(input())
length = 1
start = 1
res = 0
while True:
    end = start*10-1
    if end > n:
        end = n
    res += ((end - start)+1)*length
    start *= 10
    length += 1
    
    if start > n:
        break

print(res)