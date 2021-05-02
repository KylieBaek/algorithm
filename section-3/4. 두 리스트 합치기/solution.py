import sys

sys.stdin = open("in1.txt", "rt")

n1 = int(input())
a = list(map(int, input().split()))
n2 = int(input())
b = list(map(int, input().split()))

# 두 리스트 다시 sort() ->  nlogn
# 이미 정렬된 두개 리스트 -> n
p1 = p2 = 0
c = []

while p1 < n1 and p2 < n2:
    if a[p1] <= b[p2]:
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2 += 1
if p1 < n1:
    c = c + a[p1:]
if p2 < n2:
    c = c + b[p2:]

print(c)
