import sys

# 그리디 -> 정렬 후 선택
sys.stdin = open("in1.txt", "rt")

# 일대일로 비교했을 때 키, 몸무게 중 적어도 하나는 큰 값으로 뽑는데 최대 인원

n = int(input())
a = []
for _ in range(n):
    h, w = map(int, input().split())
    a.append((h, w))
a.sort(reverse=True)
cnt = 0
before_w = 0
for h, w in a:
    # 키는 작으니(이미 정렬) 몸무게만 크면됨
    if w > before_w:
        cnt += 1
        before_w = w

print(cnt)
