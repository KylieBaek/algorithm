import sys
import heapq as hq

sys.stdin = open("in1.txt", "rt")
a = []
# 최소힙
# 부모 노드 값이 자식 노드 값보다 무조건 작음
while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(hq.heappop(a))
    else:
        hq.heappush(a, n)
