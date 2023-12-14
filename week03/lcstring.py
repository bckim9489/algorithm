import sys
sys.stdin = open('stdin', 'r')

str_1 = [0]+list(str(sys.stdin.readline().strip()))
str_1_len = len(str_1)
str_2 = [0]+list(str(sys.stdin.readline().strip()))
str_2_len = len(str_2)
matrix = [[0]*(str_1_len+1) for _ in range(str_2_len+1)]
result_cnt = 0
result_string = ""
result_y_x = ()
for i in range(str_2_len):
    for j in range(str_1_len):
        if i == 0 and j == 0:
            matrix[i][j] = 0
        elif str_2[i] == str_1[j]:
            matrix[i][j] = matrix[i-1][j-1] + 1
            if result_cnt < matrix[i][j]:
                result_cnt = matrix[i][j]
                result_y_x = (i, j)
        else :
            matrix[i][j] = 0

for j in range(result_y_x[1], result_y_x[1]-result_cnt, -1):
    result_string = str_1[j]+result_string
