import sys
sys.setrecursionlimit(10**9)
sys.stdin = open('stdin', 'r')
input_data = []

while True:
    try:
        input_data.append(int(sys.stdin.readline()))
    except:
        break

def postorder(input_data, start, end):      
        mid = end+1
        if start > end:
             return

        for i in range(start+1, end+1):
            if input_data[start] < input_data[i]:
                mid = i
                break

        postorder(input_data, start+1, mid-1)
        postorder(input_data, mid, end)        
        print(input_data[start])


postorder(input_data, 0, len(input_data)-1)

