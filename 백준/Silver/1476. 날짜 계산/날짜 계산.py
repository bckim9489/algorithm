import sys

e, s, m = map(int, sys.stdin.readline().split())
e -= 1
s -= 1
m -= 1
e_lim, s_lim, m_lim = 15, 28, 19

year = 0
while True:
    if year % e_lim == e and year % s_lim == s and year % m_lim == m:
        print(year+1)
        break
    year += 1