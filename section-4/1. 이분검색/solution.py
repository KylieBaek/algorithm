import sys

sys.stdin = open("in1.txt", "rt")
# 이분 검색 -> 정렬된 상태!
# log2n
n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
# print(a.index(m)+1)

lt = 0
rt = n - 1
while lt <= rt:
    mid = (lt + rt) // 2
    if a[mid] == m:
        print(mid + 1)
        break
    elif a[mid] > m:
        rt = mid - 1
    else:
        lt = mid + 1
