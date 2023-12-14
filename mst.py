import sys
sys.stdin = open('stdin', 'r')
v, e = map(int, sys.stdin.readline().split())

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    if a > b:
        parent[a] = b

parent = [0]*(v+1)
edges = []
result = 0

for i in range(1, v+1):
    parent[i] = i

for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        
print(result)