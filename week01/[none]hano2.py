import sys
sys.stdin = open('stdin', 'r')
n = int(sys.stdin.readline())
dp = {}
def hanoi(panel, st, ed):
    if panel == 1:
        return f'{st} {ed}\n'
    if (panel, st, ed) in dp:
        return dp[(panel, st, ed)]
    dp[(panel, st, ed)] = ''.join([f'{hanoi(panel-1, st, 6-st-ed)}{st} {ed}\n{hanoi(panel-1, 6-st-ed, ed)}'])
    return dp[(panel, st, ed)]

print(pow(2,n)-1)
if n <= 20:
    print(hanoi(n, 1, 3))