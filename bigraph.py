import sys
sys.setrecursionlimit(10**9)
sys.stdin = open('stdin', 'r')
k = int(sys.stdin.readline())

def dfs(graph, start, color_switch):
    visited[start] = True
    color[start] = color_switch
    
    for next_node in graph[start]:
        if not visited[next_node]:
            result = dfs(graph, next_node, color_switch*-1)
            if not result:
                return False
            
        if visited[next_node]:
            if color[start] == color[next_node]:
                return False
        
    return True
    

for _ in range(k):
    V, E = map(int, sys.stdin.readline().split())
    graph  = {}
    
    visited = [False]*(V+1)
    for __ in range(E):
        u, v = map(int, sys.stdin.readline().split())
        if u not in graph:
            graph[u]=[v]
        else :
            graph[u].append(v)

        if v not in graph:
            graph[v]=[u]
        else :
            graph[v].append(u)
    
    for h in graph.keys():
        color = [0]*(V+1) #index 0 안씀
        if visited[h] == 0:
            result = dfs(graph, h, 1)
            if not result:
                break

    print("YES" if result else "NO")
