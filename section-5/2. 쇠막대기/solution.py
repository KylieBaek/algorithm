import sys

sys.stdin = open("in1.txt", "rt")

s = input()
cnt = 0
stack = []


for i in range(len(s)):
    print(stack)
    print(cnt)
    if s[i] == '(':
        stack.append(s[i])
    else:
        if s[i - 1] == '(':  # 레이저
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()  # 쇠막대기 끝
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