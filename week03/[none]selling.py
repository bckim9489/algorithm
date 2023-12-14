'''
-다시풀기-
[NO : 2098]
* Solution Tip:
    1. 비트마스크 + DP + DFS는 필수로 써야 통과가 된다
    2. 어느 지점에서 시작해서 돌아와도 최소 코스트는 같다.(하나의 순회 경로만 보면 됨)

* Issue :
    1. [해결 전략]
        
    2. [구현]

* Comment :
    1. 플로이드-워설 알고리즘 개념과 비슷하게 느꼈다.
'''

'''
* 비트마스킹 
    visted (0001)                   visted (0001)
&   1 << n (n = 1, 10)          |   1 << n (n = 1, 10)
---------                       ---------
    0001                             0001
    0010                        +    0010
---------                       ---------
    0000                             0011        
'''
import sys
sys.setrecursionlimit(10**9)
sys.stdin = open('stdin', 'r')

n = int(sys.stdin.readline())
graph = []
dp = {}

for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    graph.append(row)

def dfs(now_node, visited):
    
    if visited == (1 << n) -1:
        #base case: 다 방문할 경우
        if graph[now_node][0] != 0:
            return graph[now_node][0]
        return sys.maxsize

    if (now_node, visited) in dp:
        if dp[(now_node, visited)]:
            return dp[(now_node, visited)]
        
    cost_min = sys.maxsize

    for next_node in range(1, n):
        if graph[now_node][next_node] == 0 or (visited & (1 << next_node)) != 0:
            continue
        cost = dfs(next_node, (visited | (1 << next_node)))+ graph[now_node][next_node]
        cost_min = min(cost_min, cost)

    dp[(now_node, visited)] = cost_min
    return cost_min

print(dfs(0,1))
