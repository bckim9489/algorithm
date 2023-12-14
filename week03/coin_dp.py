import sys
sys.stdin = open('stdin', 'r')

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    row = [0]+list(map(int, sys.stdin.readline().split()))
    price = int(sys.stdin.readline())

    costs = [1]+[0]*(price)
    for i in range(1, n+1):
        for j in range(1, price+1):
            if j >= row[i]:
                costs[j] += costs[j-row[i]]
    print(costs[price])