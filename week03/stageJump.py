import sys
sys.stdin = open('stdin', 'r')

n = int(sys.stdin.readline())
stage = [int(sys.stdin.readline()) for _ in range(n)]

total_score = stage[0]
dp = [[0]*2 for _ in range(n)]
'''
for i in range(1, n):
'''
print(dp)