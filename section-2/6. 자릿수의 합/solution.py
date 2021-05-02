import sys

sys.stdin = open("in1.txt", "rt")
n = int(input())
a = list(map(int, input().split()))


def digit_sum(x):
    sum = 0
    for i in str(x):  # int는 not iterable
        sum += int(i)
    return sum


max = -2147000000
for x in a:
    tot = digit_sum(x)
    if tot > max:
        max = tot
        res = x

print(res)
