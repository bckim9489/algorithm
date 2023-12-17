''' 
# 좀 더 이해하기 쉬운 방법
sieve = [False]*(MAX+1)
sieve[0] = sieve[1] = True
for i in range(2, MAX+1):
    if not sieve[i]:
        j = i+i #자기 자신을 제외한 i배수
        while j <= MAX:
            sieve[j] = True
            j += i #다음 i배수
'''