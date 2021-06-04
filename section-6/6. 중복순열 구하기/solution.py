import sys

sys.stdin = open("in1.txt", "rt")
# input = sys.stdin.readline() 입력양 많을 때


def DFS(L):
    if L == m:
        for j in range(m):
            print(res[j], end=' ')
        print()
        return

    for i in range(1, n + 1):
        res[L] = i
        DFS(L + 1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    a = list(range(1, n + 1))
    res = [0] * m

    DFS(0)
