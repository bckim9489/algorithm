d = {}
def move(a, b, c):
    if a == 1:
        return f'{b} {c}\n' 
    if (a, b) in d:
        return d[(a, b)]  
    d[(a, b)] = ''.join([move(a-1, b, 6-b-c), f'{b} {c}\n', move(a-1, 6-b-c, c)])
    return d[(a, b)]
a = int(input())
print(pow(2,a)-1)
if a <= 20:
    print(move(a, 1, 3))