import sys

sys.stdin = open("in1.txt", "rt")


# tot -sum = 또 다른 부분집합의 합
# L : index of a
# sum: 누적 합

def DFS(L, sum):
    global switch
    if switch: return
    if sum > (tot // 2):  # 탐색할 필요 없는 경우
        return

    if L == n:
        if sum == (tot - sum):
            print("YES")
            # sys.exit(0)
            switch = 1
    else:
        DFS(L + 1, sum + a[L])
        DFS(L + 1, sum)


if __name__ == "__main__":
    switch = 0
    n = int(input())
    a = list(map(int, input().split()))
    tot = sum(a)
    DFS(0, 0)
    if switch == 0:
        print("NO")
