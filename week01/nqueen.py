import sys
sys.stdin = open('stdin', 'r')

n = int(sys.stdin.readline())

board = [0]*n
cnt = 0

def set_queen(idx):
    global cnt

    if n == idx:
        cnt +=1
        return

    for i in range(n):
        board[idx] = i
        
        if chk(idx):
            set_queen(idx+1)

def chk(idx):
    for j in range(idx):
        if board[idx] == board[j] or abs(idx-j) == abs(board[idx]- board[j]):
            return False
    return True

set_queen(0)
print(cnt)