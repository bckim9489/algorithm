'''
플로이드 워셜은 거쳐가는 중간값을 기준으로 

graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j]) 

인 알고리즘이다.
'''
import sys
sys.stdin = open('stdin', 'r')

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[float('inf')]*(n) for _ in range(n)]

for i in range(n):
    graph[i][i] = 0


for _ in range(m):
    u, v, cost = map(int, sys.stdin.readline().split())
    if graph[u-1][v-1] > cost:
        graph[u-1][v-1] = cost

print(*graph, sep='\n')
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

for i in range(n):
    for j in range(n):
        if graph[i][j] == float('inf'):
            graph[i][j] = 0

for i in graph:
    print(*i)
