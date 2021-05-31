import sys

sys.stdin = open("in1.txt", "rt")


# 상태트리 dfs
def DFS(v):
    if v == n + 1:
        for i in range(1, n + 1):
            if chk[i]:
                print(i, end=' ')
        print()
    else:
        chk[v] = True
        DFS(v + 1)
        chk[v] = False
        DFS(v + 1)


if __name__ == "__main__":
    n = int(input())
    chk = [False] * (n + 1)
    DFS(1)
