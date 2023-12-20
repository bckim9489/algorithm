'''
[LV.1 스킬체크] 2번 / 파기일자
[memo] 
    1. IDE 없이 하는게 힘들었따....ㅠㅠ
'''
def solution(today, terms, privacies):
    answer = []
    dic_t = {}
    t_year, t_month, t_day = map(int, today.split('.'))

    for elem in terms:
        mode, expire_m = elem.split(' ')
        dic_t[mode] = expire_m

    for idx, elem_p in enumerate(privacies):
        priv_date, mode = elem_p.split(' ')
        priv_year, priv_month, priv_day = priv_date.split('.')

        expire_month = int(priv_month)
        expire_year = int(priv_year)
        expire_day = int(priv_day)

        if int(dic_t[mode]) > 12:
            add_month = int(dic_t[mode]) % 12
            add_year = int(dic_t[mode]) // 12
            expire_month += add_month
            expire_year += add_year
        else :
            expire_month += int(dic_t[mode])

        if expire_month > 12:
            expire_month -= 12
            expire_year += 1

        if t_year > expire_year:
            answer.append(idx+1)
            continue
        elif t_year == expire_year and t_month >expire_month :
            answer.append(idx+1)
            continue
        elif t_year == expire_year and t_month ==expire_month and t_day >= expire_day:
            answer.append(idx+1)
            continue

    return answer