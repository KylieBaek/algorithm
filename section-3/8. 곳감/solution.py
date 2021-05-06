import sys
from collections import deque
import copy

sys.stdin = open("in1.txt", "rt")
n = int(input())
a = list(list(map(int, input().split())) for _ in range(n))

m = int(input())


def rotate_right(arr, count):
    while count > 0:
        count -= 1
        x = arr.pop()
        arr.insert(0, x)
    return arr


def rotate_left(arr, count):
    arr = deque(arr)
    while count > 0:
        count -= 1
        x = arr.popleft()
        arr.append(x)
    return arr


for _ in range(m):
    i, is_right, cnt = map(int, input().split())
    if is_right:
        arr = copy.deepcopy(a[i - 1])
        arr = rotate_right(arr, cnt)
    else:
        arr = copy.deepcopy(a[i - 1])
        arr = rotate_left(arr, cnt)
    a[i - 1] = arr


    # solution 2
    # if is_right == 0:
    #     for _ in range(cnt):
    #         a[i - 1].append(a[i - 1].pop(0))
    # else:
    #     for _ in range(cnt):
    #         a[i - 1].insert(0, a[i - 1].pop())

# 모래시계 합구하기
s = 0
e = n - 1
res = 0
for i in range(n):
    for j in range(s, e + 1):
        res += a[i][j]

    if i < n // 2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(res)
