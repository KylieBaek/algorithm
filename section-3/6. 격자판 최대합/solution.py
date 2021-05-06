import sys

sys.stdin = open("in1.txt", "rt")
# 행, 열, 대각선 합 중 가장 큰 값
n = int(input())
a = list(list(map(int, input().split())) for _ in range(n))
# for i in range(n):
#     a[i] = list(map(int, input().split()))
largest = -21470000000

for i in range(n):
    s1 = s2 = 0
    for j in range(n):
        s1 += a[i][j]  # 행
        s2 += a[j][i]  # 열
    if largest < s1:
        largest = s1
    elif largest < s2:
        largest = s2

s1 = s2 = 0
for i in range(n):
    s1 += a[i][i]      # 대각선\
    s2 += a[i][n - i - 1]  # 대각선/

if largest < s1:
    largest = s1
elif largest < s2:
    largest = s2

print(largest)
