'''
[LV.2 스킬체크] 1번 / 패치 순서
[memo] 
    없음
'''
def solution(progresses, speeds):
    answer = []
    while progresses:
        cnt = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        for _ in range(len(progresses)):
            if progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                cnt += 1

        if cnt != 0:
            answer.append(cnt)

    return answer