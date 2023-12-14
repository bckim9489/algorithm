import sys
sys.stdin = open('stdin', 'r')

n, k = map(int, sys.stdin.readline().split())
item_list = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    w, v = map(int, sys.stdin.readline().split())
    for j in range(1, k+1):
        if (j < w):
            item_list[i][j] = item_list[i-1][j]
        else :
            item_list[i][j] = max(item_list[i-1][j], item_list[i-1][j-w] + v)
    
print(item_list[n][k])