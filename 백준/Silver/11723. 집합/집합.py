import sys
m = int(input())
bitmask = 0

def calc(cmd):
    global bitmask
    command = cmd[0]
    if command == 'add':
        bitmask = bitmask | (1<<int(cmd[1]))
        return
    if command == 'check':
        if bitmask & (1<<int(cmd[1])):
            print(1)
        else :
            print(0)
        return
    if command == 'remove':
        bitmask = bitmask & ~(1<<int(cmd[1]))
        return
    if command == 'toggle':
        bitmask = bitmask ^ (1<<int(cmd[1]))
        return
    if command == 'all':
        bitmask = (1 << 21) - 1
        return
    if command == 'empty':
        bitmask = 0
        return
    
for _ in range(m):
    cmd = sys.stdin.readline().split()
    calc(cmd)