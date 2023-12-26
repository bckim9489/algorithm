'''
[LV.3] 베스트 앨범
[memo] 
    1. IDE없이....딕셔너리와 리스트를 정렬하는 법을 배웠다.
    2. sorted_dic[itm].sort(key=lambda x:(x[1], -x[0]), reverse=True) 이걸 못해서 10분을 날렸다.
'''
def solution(genres, plays):
    answer = []
    g_dic = {}
    for genre in genres:
        g_dic[genre] = [0]
    for idx, genre in enumerate(genres):
        g_dic[genre][0] += plays[idx]
        g_dic[genre].append((idx, plays[idx]))
    
    sorted_dic = dict(sorted(g_dic.items(), key= lambda item:item[1], reverse=True))
    for itm in sorted_dic:
        sorted_dic[itm].pop(0)
        sorted_dic[itm].sort(key=lambda x:(x[1], -x[0]), reverse=True)
    
    for itm in sorted_dic:
        answer.append(sorted_dic[itm][0][0])
        if len(sorted_dic[itm]) > 1:
            answer.append(sorted_dic[itm][1][0])     
        
    return answer