import sys

# 결정 알고리즘 (특정 범위안에 답이 있음) -> 이분 검색 이용하기
sys.stdin = open("in1.txt", "rt")


def count(length):
    cnt = 0
    for x in a:
        cnt += (x // length)
    return cnt


k, n = map(int, input().split())
a = []
largest = 0
for i in range(k):
    tmp = int(input())
    a.append(tmp)
    largest = max(largest, tmp)



# 이분 검색
lt = 1
rt = largest
res = 0

while lt <= rt:
    mid = (lt + rt) // 2
    if count(mid) >= n:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)
