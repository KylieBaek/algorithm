import sys

sys.stdin = open("in1.txt", "rt")
# 후위연산식 -> 연산한 결과 출력

stack = []
a = input()
temp = 0

for x in a:
    if x.isdecimal():
        # x 는 string!! int화해야 숫자됨
        stack.append(int(x))
    else:
        second_num = stack.pop()
        first_num = stack.pop()
        if x == '+':
            temp = (first_num + second_num)
        elif x == '-':
            temp = (first_num - second_num)
        elif x == '/':
            temp = (first_num / second_num)
        elif x == '*':
            temp = (first_num * second_num)
        stack.append(temp)

print(stack[0])
