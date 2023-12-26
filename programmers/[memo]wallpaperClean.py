'''
[AI 추천] 바탕화면 정리
[memo] 
    없음
'''
import sys
def solution(wallpaper):
    answer = []
    conv_arr = []
    for idx in range(len(wallpaper)):
        conv_arr.append(list(map(str, wallpaper[idx])))
        
    start_x = sys.maxsize
    start_y = sys.maxsize
    end_x   = 0
    end_y   = 0
    
    for idx, arr in enumerate(conv_arr):
        for i, itm in enumerate(arr):
            if itm == '#':
                start_x = min(start_x, idx)
                start_y = min(start_y, i)
                end_x   = max(end_x, idx+1)
                end_y   = max(end_y, i+1)
            
    answer.append(start_x)
    answer.append(start_y)
    answer.append(end_x) 
    answer.append(end_y)

    return answer