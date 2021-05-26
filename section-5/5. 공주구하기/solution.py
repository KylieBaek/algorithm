import sys
from collections import deque

sys.stdin = open("in1.txt", "rt")
n, k = map(int, input().split())
q = deque(list(range(1, n + 1)))

while q:
    for _ in range(k - 1):
        current = q.popleft()
        q.append(current)
    q.popleft()  # k번째

    if len(q) == 1: # 하나있을때 출력
        print(q[0])
