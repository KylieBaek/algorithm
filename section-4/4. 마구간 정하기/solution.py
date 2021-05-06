import sys

# 결정 알고리즘 (특정 범위안에 답이 있음) -> 이분 검색 이용하기
sys.stdin = open("in1.txt", "rt")


def count(length):
    cnt = 1
    end_pt = a[0]  # 말 한마리를 첫 마구간에 배치
    for i in range(1, n):
        if a[i] - end_pt >= length:
            cnt += 1
            end_pt = a[i]
    return cnt


# 가장 가까운 두 말의 거리 최대 -> 임의의 두 말의 거리는 그것보다 커야함
n, c = map(int, input().split())
a = []
for _ in range(n):
    a.append(int(input()))
a.sort()

lt = a[0]
rt = a[n - 1]
res = 0

while lt <= rt:
    mid = (lt + rt) // 2
    if count(mid) >= c:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(res)
