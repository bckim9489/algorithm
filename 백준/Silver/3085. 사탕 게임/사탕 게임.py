import sys

result = 1

n = int(input())
board = []
dx, dy = [1, 0], [0, 1]
for _ in range(n):
    row = list(sys.stdin.readline().strip())
    board.append(row)

def chkCndy(n):
    res = 1

    for i in range(n):     
        cndyDupl = 1
        for j in range(1, n):
            if board[i][j] == board[i][j-1]:
                cndyDupl += 1
            else :
                cndyDupl = 1
            
            res = max(res, cndyDupl)
        
        cndyDupl = 1
        for j in range(1, n):
            if board[j][i] == board[j-1][i]:
                cndyDupl += 1
            else :
                cndyDupl = 1
            
            res = max(res, cndyDupl)

    return res

for i in range(n):
    for j in range(n):
        for k in range(2):
            nx, ny = dx[k]+i, dy[k]+j
            if 0 <= nx < n and 0 <= ny < n:
                board[i][j], board[nx][ny] = board[nx][ny], board[i][j]
                result = max(result, chkCndy(n))
                board[i][j], board[nx][ny] = board[nx][ny], board[i][j]

print(result)