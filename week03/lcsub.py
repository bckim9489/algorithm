import sys
sys.stdin = open('stdin', 'r')

str_1 = list(str(sys.stdin.readline().strip()))
str_1_len = len(str_1)
str_2 = list(str(sys.stdin.readline().strip()))
str_2_len = len(str_2)  
matrix = [[0]*(str_1_len+1) for _ in range(str_2_len+1)]

for i in range(1, str_2_len+1):
    for j in range(1, str_1_len+1):
        if str_1[j-1] == str_2[i-1]:
            matrix[i][j] = matrix[i-1][j-1] +1
        else :
            matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])

print(matrix[str_2_len][str_1_len])