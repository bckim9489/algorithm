import sys
sys.stdin = open('stdin', 'r')
from collections import deque

n, k = map(int, sys.stdin.readline().split())

wallet = []
cnt = 0
memo = {}

for _ in range(n):
    worth = int(sys.stdin.readline())
    wallet.append(worth)

wallet.sort(reverse=True)

def bfs():
    queue = deque()
    for i in wallet:
        queue.append((i, 1))
        memo[i] = 1

    while queue:
        now_coin, now_cost = queue.popleft()
        
        if now_coin == k:
            return now_cost

        for i in range(n):
            next_coin = now_coin+wallet[i]

            if next_coin <= k:
                if next_coin in memo:
                    continue

                next_cost = now_cost + 1
                memo[next_coin] = next_cost
                queue.append((next_coin, next_cost))

    return -1

print(bfs())