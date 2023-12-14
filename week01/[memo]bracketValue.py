'''
[NO : 2504]
* Solution Tip:
    1. 각 case에 대해 전부 만들어줘야 됨
    2. 열리는 괄호가 시작될 경우에 곱셈을 해주고 닫힐 경우에서 두가지 케이스로 나뉜다.( '(', '[')
    3. 닫히는 괄호일 경우 스택에서 최근 괄호가 맞이 않는 경우 false
    4. 스택에 아직 남아 있고 최근 괄호가 지금 괄호랑 짝이 맞는 경우에서,
        이전 단어배열의 괄호가 짝이 맞는 괄호일 경우 지금까지의 tmp를 더해주며 앞서 열리는 괄호에서 곱셈을 해준 상황을 무마한다.
* Issue :
    1. [해결 전략]
        1) 전략부터 잘 떠오르지 않았다. 스택을 쓰는 것은 알았지만 모든 케이스에 대해 작성해야 하는지에 대한 의문이 있었다.
        2) 결국 모든 케이스에서 작성이 필요하다는 결론을 내린 뒤 구현에서 문제가 생겼다.
    2. [구현]
        1) 스택에 열리는 괄호를 넣고 닫히는 괄호를 만나면 팝 해주는 구현까지 갔으나 연산에 대한 구현이 떠오르지 않고 시간이 초과되었다.
        2) 풀이를 보니 tmp와 같은 임시 변수를 하나 만들고 구현에 들어갔고 연산 값에 대한 처리는 문제에 나와있었다.
* Comment :
    없음

'''
import sys
sys.stdin = open('stdin', 'r')
stack = []

n = str(sys.stdin.readline().strip())

tmp = 1
result = 0

for idx, tag in enumerate(n):
    if tag == '(':
        tmp *= 2
        stack.append(tag)
        continue

    if tag == '[':
        tmp *= 3
        stack.append(tag)
        continue

    if tag == ')':
        if not stack or stack[-1] != '(':
            result = 0
            break
        if n[idx-1] == '(':
            result += tmp
        tmp //= 2
        stack.pop()
        continue

    if tag == ']':
        if not stack or stack[-1] != '[':
            result = 0
            break
        if n[idx-1] == '[':
            result += tmp
        tmp //= 3
        stack.pop()
    
if stack:
  print(0)
else:
  print(result)