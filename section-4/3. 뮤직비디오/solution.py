import sys

# 결정 알고리즘 (특정 범위안에 답이 있음) -> 이분 검색 이용하기
# DVD 1장의 lt(최소용량 =1) ~ rt(전체 합=45)
sys.stdin = open("in1.txt", "rt")


def count(capacity):
    cnt = 1
    sum = 0
    for x in a:
        if sum + x > capacity:
            cnt += 1
            sum = x
        else:
            sum += x

    return cnt


n, m = map(int, input().split())
a = list(map(int, input().split()))
largest = max(a)

lt = 1
rt = sum(a)
res = 0

while lt <= rt:
    mid = (lt + rt) // 2
    if mid >= largest and count(mid) <= m: # m개보다 작으면 당연히 m개도 가능함
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1

print(res)