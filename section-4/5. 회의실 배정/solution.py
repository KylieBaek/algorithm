import sys

# 그리디 -> 정렬 후 선택
sys.stdin = open("in1.txt", "rt")

# 최대 회의실 구하기 -> 빨리 끝나야 함 -> 끝나는 시간으로 정렬
n = int(input())
meeting = []
for i in range(n):
    s, e = map(int, input().split())
    meeting.append((s, e))
meeting.sort(key=lambda x: (x[1], x[0]))

end_time = 0
cnt = 0
for s, e in meeting:
    if s >= end_time:
        end_time = e
        cnt += 1

print(cnt)
