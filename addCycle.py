import sys
sys.setrecursionlimit(10**9)
a = int(sys.stdin.readline())

ans = ""
cnt = 0
def foo(a=int, number=int):
    global cnt
    sum_num = ""
    if number < 10:
       number = "0"+str(number)
       sum_num = number
    else :
        sum_num = str(int(str(number)[0]) + int(str(number)[1]))
        if int(sum_num) < 10:
            sum_num = '0'+sum_num

    new_num = int(str(number)[1]+str(sum_num)[1])
    cnt += 1

    if int(a) == int(new_num):
        print(cnt)
        quit()
    else :
        return foo(a, new_num)

foo(a, a)

