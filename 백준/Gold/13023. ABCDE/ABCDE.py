import sys

n, m = map(int, sys.stdin.readline().split())

g = [[0]*n for _ in range(n)]
f = [[] for _ in range(n)]
edges = []
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    g[a][b] = 1
    g[b][a] = 1
    
    f[a].append(b)
    f[b].append(a)

    edges.append((a,b))
    edges.append((b,a))

m*=2

for i in range(m):
    for j in range(m):
        a, b = edges[i]
        c, d = edges[j]
        if a == b or a == c or a == d or b == c or b == d or c == d :
            continue
        if not g[b][c]:
            continue
        for e in f[d]:
            if a == e or b == e or c == e or d == e:
                continue
            print(1)
            sys.exit()

print(0)