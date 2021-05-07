import sys

sys.stdin = open("in1.txt", "rt")
# 가장 긴 증가수열 만들기
n = int(input())
a = list(map(int, input().split()))

lt = 0
rt = n - 1
last = 0 # 증가수열의 가장 마지막
res = ''
tmp = []

while lt <= rt:
    if a[lt] > last:
        tmp.append((a[lt], 'L'))
    if a[rt] > last:
        tmp.append((a[rt], 'R'))

    # 둘 중 작은거 넣기
    tmp.sort()

    # 둘다 작으면 끝남
    if len(tmp) == 0:
        break
    else:
        res = res + tmp[0][1]
        last = tmp[0][0]
        if tmp[0][1] == 'L':
            lt += 1
        else:
            rt -= 1
    tmp.clear()

print(len(res))
print(res)
