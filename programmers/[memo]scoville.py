'''
[LV.2 스킬체크] 2번 / 스코빌
[memo] 
    1.IDE없이 heapq 를 쓰려니 힘들다... 기본적인 표준 라이브러리는 외워버리자
'''
import heapq
def solution(scoville, K):
    if min(scoville) >= K :
        return 0

    answer = 0

    heapq.heapify(scoville)
    while len(scoville) > 1:
        scov_first = heapq.heappop(scoville)
        scov_second = heapq.heappop(scoville)
        scoville_make = scov_first + (scov_second*2)
        heapq.heappush(scoville, scoville_make)
        answer += 1

        if scoville[0] >= K:
            return answer

    return -1