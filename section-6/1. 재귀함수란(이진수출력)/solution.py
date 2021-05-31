import sys

sys.stdin = open("in1.txt", "rt")


# 이진수 만들기 dfs

def DFS(x):
    if x == 0:
        return
    DFS(x // 2)
    print(x % 2, end='')


if __name__ == '__main__':
    DFS(int(input()))
