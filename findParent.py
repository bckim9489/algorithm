import sys
sys.stdin = open('stdin', 'r')

n = int(sys.stdin.readline())
tree = {i:[] for i in range(n+1)}
parent_list = [0]*(n+1)
visited = [False]*(n+1)
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(tree, start, visited):
    if not tree[start]:
        return start
    
    if not visited[start]:
        visited[start] = True
        parent_list[start]
        
        for next_node in range(len(tree[start])):
            node = tree[start][next_node]
            result = dfs(tree, node, visited)
            parent_list[result] = start
    
    return start

dfs(tree, 1, visited)
for ans in parent_list[2:]:
    print(ans)