import sys

n, k = map(int, sys.stdin.readline().split())

if n >= k:
    print(0)
    quit()

elec_list = list(map(int, sys.stdin.readline().split()))
p_socket = []

while True:
    if len(p_socket) == n:
        break

    if len(elec_list) == 0:
        print(0)
        quit()
    
    item = elec_list.pop(0)
    if item in p_socket:
        continue

    p_socket.append(item)
    
def isLastest(a):
    if a in elec_list:
        result = elec_list.index(a)
        return result
    else :
        return k
    
cnt = 0

while elec_list:
    
    now_item = elec_list.pop(0)
    

    if now_item in p_socket:
        continue

    unPlug_item = 0
    unPlug_item_idx = 0
    
    for i in p_socket:
        if unPlug_item_idx <= isLastest(i):
            unPlug_item_idx = isLastest(i)
            unPlug_item = i
    
    p_socket.pop(p_socket.index(unPlug_item))
    p_socket.append(now_item)
    cnt += 1
    
print(cnt)