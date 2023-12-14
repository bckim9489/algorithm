
import random

class DisjointSet:
    def __init__(self, nodeCnt):
        self.U = []
        for i in range(nodeCnt):
            self.U.append(i)
    
    def equal(self, p, q):
        if(p == q):
            return True
        else:
            return False
    
    def find(self, i):
        j = i
        while(self.U[j] != j):
            j = self.U[j]
        return j
    
    def union(self, p, q):
        if(p < q):
            self.U[q] = p
        else:
            self.U[p] = q

def kruskal(n, E):
    F = []
    dset = DisjointSet(n)
    while (len(F) < n-1):
        edge = E.pop(0)
        i, j = edge[0], edge[1]
        p = dset.find(i)
        q = dset.find(j)
        if(not dset.equal(p, q)):
            dset.union(p, q)
            F.append(edge)
    return F
if __name__ == "__main__":
    n = 5
    totalCost = 0;
    E = [
        [0, 1, 1],
        [2, 4, 2],
        [0, 2, 3],
        [1, 2, 3],
        [2, 3, 4],
        [3, 4, 5],
        [1, 3, 6],
    ]

    F = kruskal(n, E)
    
    for i in range(len(F)):
        print(F[i])
        totalCost += F[i][2]
    
    print(totalCost)

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

if __name__ == "__main__":
    #v 노드 개수, e 간선개수
    v, e = map(int, input().split())
    parent = [0]*(v+1)
    edges = []
    result = 0

    for i in range(1, v+1):
        parent[i] = i

    for _ in range(e):
        a, b, cost = map(int, input().split())
        edges.append((cost, a, b))

    edges.sort()

    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost
            
    print(result)