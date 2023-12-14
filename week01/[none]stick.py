import sys
sys.stdin = open('stdin', 'r')

n = int(sys.stdin.readline())

stack = []

for i in range(n):
    height = int(sys.stdin.readline())
    stack.append(height)

result = []

for i in range(n):
    now_stick = stack.pop()
    if not result:
        result.append(now_stick)
    else :
        if result[-1] < now_stick:
            result.append(now_stick)

print(len(result))
    
