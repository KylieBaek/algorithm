import sys

sys.stdin = open("in1.txt", "rt")
res = ''
stack = []
# +- 는 */ 보다 우선순위가 낮음 stack 에서 우선순위 비교 숫자는 stack에 넣지 않고 출력한다.
# +- 는 stack.pop()

a = input()
for x in a:
    if x.isdecimal():  # 10진수
        res += x
    else:
        if x == '(':
            stack.append(x)
        elif x == '*' or x == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                res += stack.pop()  # 왼쪽꺼 먼저 (우선순위 높음)
            stack.append(x)
        elif x == '+' or x == '-':
            while stack and (stack[-1] != '('): # 괄호안에 + - 인경우 멈춤
                res += stack.pop()
            stack.append(x)
        elif x == ')':
            while stack and (stack[-1] != '('):
                res += stack.pop()
            stack.pop()


while stack:
    res += stack.pop()

print(res)
