'''
[고득점 kit] 타겟넘버
[memo] 
    없음
'''
import sys
sys.setrecursionlimit(10**9)
                     
def dfs(result, idx, cnt, numbers, target):
        if result < target:
            return
        
        if result == target:
            cnt += 1
            return
        
        result = sum(numbers)
        
        for arr_idx, number in enumerate(numbers):
            numbers[arr_idx] *= -1
            dfs(result, arr_idx+1, cnt, numbers, target)
            numbers[arr_idx] *= -1
        
        return cnt
    
def solution(numbers, target):
    answer = 0
    visited = [False for _ in numbers]
    
    answer = dfs(sys.maxsize, 0, 0, numbers, target)
    return answer

print(solution([4, 1, 2, 1], 2))