import sys

sys.stdin = open("in1.txt", "rt")
# 5자리 회문수 구하기

board = [list(map(int, input().split())) for _ in range(7)]
cnt = 0
for i in range(3):
    for j in range(7):
        # 행
        tmp = board[j][i:i + 5]
        if tmp == tmp[::-1]:
            cnt += 1

        # 열
        for k in range(5 // 2):  # 5자리이므로 두 개씩 비교하기
            if board[i + k][j] != board[i + 5 - k - 1][j]:
                break
        else:
            cnt += 1

print(cnt)
