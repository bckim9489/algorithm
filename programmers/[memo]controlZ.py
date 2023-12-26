'''
[AI 추천] 컨트롤 제트
[memo] 
    1. 스택에 넣어서 풀려다 그냥 풀었다.
'''
def solution(s):
    answer = 0
    stack = list(s.split(" "))
    for idx, itm in enumerate(stack):
        if itm == 'Z':
            answer -= int(stack[idx-1])
        else :
            answer += int(itm)
            
    return answer