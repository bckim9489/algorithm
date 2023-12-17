'''
[PCCP 기출문제] 1번 / 붕대 감기
[memo] 
    1. 프로그래머스에서 외부 IDE 없이 짜는 연습이 필요.
    2. 자동완성에 너무 익숙해져 있었음. 고칠 필요 있음.
'''

def solution(bandage, health, attacks):

    now_health = health
    t, x, y = bandage
    last_time = attacks[-1][0]
    time_ticks = 0
    at_t = {}
    for itm in attacks:
        at_t[itm[0]] = itm[1]
    
    bonus_ticks = 0
    
    while time_ticks <= last_time:
        if time_ticks in at_t:
            now_health -= at_t[time_ticks]
            bonus_ticks = 0
            
            if now_health < 1:
                return -1
        else :
            bonus_ticks +=1
            if bonus_ticks != t:
                now_health += x
                
            else :
                now_health += (x+y)
                bonus_ticks = 0
                
            if now_health > health:
                now_health = health
                
        time_ticks += 1
            
    return now_health