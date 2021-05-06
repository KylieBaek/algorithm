import sys

sys.stdin = open("in1.txt", "rt")
n = int(input())
a = list(list(map(int, input().split())) for _ in range(n))
# 격자판 다이아몬드 합 구하기


sum = 0

# # 테두리
# sum += a[0][n // 2]
# sum += a[n // 2][0]
# sum += a[n // 2][n - 1]
# sum += a[n - 1][n // 2]

s = e = n // 2
for i in range(n):
    for j in range(s, e + 1):  # s부터e까지
        sum += a[i][j]
    if i < n // 2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1

print(sum)
