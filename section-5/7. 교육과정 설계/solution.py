import sys
from collections import deque

sys.stdin = open("in1.txt", "rt")
priorities = input()
n = int(input())

for i in range(n):
    schedule = input()
    q = deque(priorities)

    for x in schedule:  # schedule 탐색
        if x in q:  # x 가 q 에 있으면
            if x != q.popleft():
                print("#{} NO".format(i + 1))
                break
    else:
        if len(q) == 0:
            print("#{} YES".format(i + 1))
        else:
            print("#{} NO".format(i + 1))
