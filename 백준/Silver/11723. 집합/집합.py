import sys

m = int(input())
bitmask = 0

for _ in range(m):
    cmd = sys.stdin.readline().split()
    command = cmd[0]
    if command == 'add':
        bitmask = bitmask | (1<<int(cmd[1]))
        continue
    if command == 'check':
        if bitmask & (1<<int(cmd[1])):
            sys.stdout.write("1\n")
        else :
            sys.stdout.write("0\n")
        continue
    if command == 'remove':
        bitmask = bitmask & ~(1<<int(cmd[1]))
        continue
    if command == 'toggle':
        bitmask = bitmask ^ (1<<int(cmd[1]))
        continue
    if command == 'all':
        bitmask = 2097151
        continue
    if command == 'empty':
        bitmask = 0
        continue