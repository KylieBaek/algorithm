import sys

sys.stdin = open("in1.txt", "rt")
a = list(range(21))

# 구간 재배치
for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e - s + 1) // 2):
        a[s + i], a[e - i] = a[e - i], a[s + i]
a.pop(0)
for x in a:
    print(x, end=' ')

# 참고 : 슬라이스는 원본리스트는 그대로 둔채 새로운 리스트를 생성한다 


