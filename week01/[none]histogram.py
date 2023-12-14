'''
다시보기
'''
import sys
sys.stdin = open('stdin', 'r')

while True:
    row = list(map(int, sys.stdin.readline().split()))
    n = row[0]
    if n == 0:
        break

    stack = []
    max_size = 0
    for idx in range(1, n+1):        
        if stack and stack[-1][1] > row[idx]:
            while stack:
                sqr_idx, sqr_height = stack.pop()
                width = 1
                if stack:
                    width += stack[-1][0]

                size = (idx - width)*sqr_height
                max_size = max(size, max_size)

                if not stack or stack[-1][1] <= row[idx]:
                    break

        if not stack or stack[-1][1] <= row[idx]:
            stack.append((idx, row[idx]))

    while stack:
        sqr_idx, sqr_height = stack.pop()
        width = 1
        if stack:
            width += stack[-1][0]
        size = ((n+1) - width)*sqr_height
        max_size = max(size, max_size)

    print(max_size)
