'''
[LV.1 스킬체크] 1번 / 중간 문자 뽑기
[memo] 
    없음
'''
def solution(s):
    divi = ''
    divi = len(s)//2
    if len(s) % 2 == 0:
        return s[divi-1]+s[divi]
    else :
        return s[divi]