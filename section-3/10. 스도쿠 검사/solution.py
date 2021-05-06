import sys

sys.stdin = open("in1.txt", "rt")


# 행, 열, 그룹 체크리스트 3개 필요


def check(a):
    # 행, 열 탐색
    for i in range(9):
        ch1 = [0] * 10
        ch2 = [0] * 10
        for j in range(9):
            ch1[a[i][j]] = 1
            ch2[a[j][i]] = 1
        if sum(ch1) != 9 or sum(ch2) != 9:
            return False

    # 그룹 탐색
    for i in range(3):  # 0, 1,2
        for j in range(3):  # 0, 1,2
            ch3 = [0] * 10
            for k in range(3):
                for s in range(3):
                    ch3[a[i * 3 + k][j * 3 + s]] = 1
            if sum(ch3) != 9:
                return False
    return True


a = [list(map(int, input().split())) for _ in range(9)]
if check(a):
    print("YES")
else:
    print("NO")
