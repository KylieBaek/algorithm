import sys

sys.stdin = open("in1.txt", "rt")
n = int(input())
a = list(map(int, input().split()))

# 오름차순 순서로 처리 -> 이미 자신보다 작은 숫자는 고려안함

seq = [0] * n
for i in range(n):
    for j in range(n):
        if (a[i] == 0 and seq[j] == 0):
            seq[j] = i + 1
            break  # j를 break
        elif seq[j] == 0:
            a[i] -= 1

for x in seq:
    print(x, end=' ')
