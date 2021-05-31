# 전위순회 CLR
# 중위순회 LCR
# 후위순회 LRC

#    1
#   2 3
# 4 5 6 7


def DFS(v):
    if v > 7:
        return
    else:
        # 전위
        print(v, end=' ')
        DFS(v * 2)  # L
        # 중위
        # print(v, end=' ')
        DFS(v * 2 + 1)  # R
        # 후위
        # print(v, end=' ')


if __name__ == "__main__":
    DFS(1)
