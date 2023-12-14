import sys
sys.setrecursionlimit(10**9)
sys.stdin = open('stdin', 'r')
MAX = 1000000001
MIN = -1000000001

n = int(sys.stdin.readline())
calc_board = list(map(int, sys.stdin.readline().split()))
op_list = list(map(int, sys.stdin.readline().split()))

total_min = MAX
total_max = MIN
# 0: + , 1: -, 2: *, 3: //

def do_calc(a, b, op) -> int:
    
    if op == 0: return a+b
    if op == 1: return a-b
    if op == 2: return a*b
    if op == 3: return int(a/b)

def calc(result, next_num):
    global total_max
    global total_min

    if next_num == n:
        total_min = min(total_min, result)
        total_max = max(total_max, result)
        return
    
    for next_op in range(4):
        if op_list[next_op] > 0:
            op_list[next_op] -= 1
            calc(do_calc(result, calc_board[next_num], next_op), next_num+1)
            op_list[next_op] += 1


calc(calc_board[0], 1)

print(total_max)
print(total_min)





