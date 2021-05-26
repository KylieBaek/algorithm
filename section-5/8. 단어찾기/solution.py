import sys
from collections import deque

sys.stdin = open("in1.txt", "rt")
n = int(input())

hash = dict()

for _ in range(n):
    word = input()
    hash[word] = 1
for _ in range(n-1):
    word = input()
    hash[word] = 0

for key, value in hash.items():
    if value == 1:
        print(key)
        break