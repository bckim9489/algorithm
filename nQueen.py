n = int(input())
arr = [0]*15
cnt = 0

def set_queen(idx):
    global cnt

    if idx == n:
       cnt += 1
       return
    
    for i in range(n):
        arr[idx] = i
        if chk_queen(idx):
            set_queen(idx+1)

def chk_queen(idx):
    for j in range(idx):
        if arr[j] == arr[idx] or (idx-j) == abs(arr[idx]-arr[j]):
            return False
    return True

set_queen(0)
print(cnt)

''' 쉬운게 답인가
n = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200 ,73712, 365596, 2279184]
print(n[int(input())])
'''