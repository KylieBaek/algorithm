import sys

sys.stdin = open("in1.txt", "rt")

n, m = map(int, input().split())

# int to list
n = list(map(int, str(n)))

# 큰 숫자가 자기보다 앞에 있어야함
# INPUT : 9977252641
# STACK :
# 9972
# 99775 pop append
# 99776 pop append
# 9977641
# 99776 뒷 자리 제거
# stack[:-m]   0~-m 전까지

stack = []
for x in n:
    while stack and m > 0 and stack[-1] < x:
        stack.pop()
        m -= 1
    stack.append(x)

# 다 지우지 못하는 경우
if m != 0:
    stack = stack[:-m]

# string화해서 붙이기
res = ''.join(map(str, stack))
print(res)
