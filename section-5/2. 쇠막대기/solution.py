import sys

sys.stdin = open("in1.txt", "rt")

s = input()
cnt = 0
stack = []

for i in range(len(s)):
    # print(stack)
    # print(cnt)
    if s[i] == '(':
        stack.append(s[i])
    elif s[i] == ')':
        if s[i - 1] == '(':  # 레이저
            stack.pop()
            cnt += len(stack)
        elif s[i] == ')':  # 쇠막대기 끝
            stack.pop()
            cnt += 1

print(cnt)

# ()(((()())(())()))(())
# STACK
# []
# ['(']
# []
# ['(']
# ['(', '(']
# ['(', '(', '(']
# ['(', '(', '(', '(']
# ['(', '(', '(']
# ['(', '(', '(', '(']
# ['(', '(', '(']
# ['(', '(']
# ['(', '(', '(']
# ['(', '(', '(', '(']
# ['(', '(', '(']
# ['(', '(']
# ['(', '(', '(']
# ['(', '(']
# ['(']
# []
# ['(']
# ['(', '(']
# ['(']
