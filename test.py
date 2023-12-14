import sys

n = int(sys.stdin.readline())
input_matrix = []

for _ in range(n):
    input_line = str(sys.stdin.readline().strip())
    input_matrix.append(list(map(int, [*input_line])))
    
