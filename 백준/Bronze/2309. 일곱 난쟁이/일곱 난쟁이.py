import sys
MAX_INPUT=9
arr = [int(sys.stdin.readline()) for _ in range(MAX_INPUT)]
lim = 100
tmp = []

arr.sort(reverse=True)

def find_dwarf(idx, cnt):
    if cnt == 7:
        if sum(tmp) == lim:
            tmp.reverse()
            for i in tmp:
                print(i)
            exit()
        else:
            return False
    
    for i in range(idx, len(arr)):
        tmp.append(arr[i])
        find_dwarf(i+1, cnt+1)
        tmp.pop()
    
find_dwarf(0, 0)