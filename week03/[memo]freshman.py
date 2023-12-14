'''
[NO : 1946]
* Solution Tip:
    1. 문제가 괴랄해서 잘 이해해야 한다. 서류점수 순위 1등을 기준으로 정렬하고 내려가면서 면접점수 순위의 커트라인이 올라가게 하면 된다.
    2. 당연히 서류점수 순위 1등이 면접도 잘봤으면 그만큼 합격자가 줄어든다.
    3. 그러다가 면접점수 순위가 1등인 사람을 만나면 합격자를 마감한다.(서류점수 순위의 마지노선)

* Issue :
    1. [해결 전략]
        1) 처음에는 서류점수 순위와 면접점수 순위의 각각의 마지노선에서 사이에 있는 사람들을 구하면 될줄 알았는데 틀렸다.
        2) 문제를 다시 읽으니 '어느 하나라도 다른 후보자들보다 높아야 한다'라는 것이 핵심이었다.
        3) 결국 두 마지노선 순위 사이에서도 정렬에 따라 합격 커트라인이 정해지게 된다는 것으로 해결했다.

    2. [구현]
        없음

* Comment :
    1. '알고리즘 문제 해결 전략'을 읽고 처음 적용해서 풀어봤다. 책에서 나온 접근 방법 중에 나누어 생각하고 합쳐서 생각하는 방법
'''
import sys
sys.stdin = open('stdin', 'r')

t = int(sys.stdin.readline())

for i in range(t):
    print(f'case {i+1}:------------------')
    cnt = 0
    interview_deadline = 0
    n = int(sys.stdin.readline())
    candidate_list = []
    for _ in range(n):
        paper, interview = map(int, sys.stdin.readline().split())
        if paper == 1:
            interview_deadline = interview
        if interview == 1:
            paper_deadline = paper
        
        candidate_list.append((paper, interview))
    
    candidate_list.sort()
    for paper_score, interview_score in candidate_list[:paper_deadline]:
        if interview_score <= interview_deadline:
            interview_deadline = interview_score
            cnt +=1
            print(paper_score, interview_score)

    print(cnt)
        
    
    

    
