import sys

sys.stdin = open("in1.txt", "rt")


def DFS(L, money):
    global min_count

    if L >= min_count: # cut edge tech
        return
    if money > m:
        return
    if money == m:
        if L < min_count:
            min_count = L
    else:
        for i in range(n):
            DFS(L + 1, money + coins[i])


if __name__ == "__main__":
    n = int(input())
    coins = list(map(int, input().split()))
    coins.sort(reverse=True)
    m = int(input())
    min_count = 2147000000

    DFS(0, 0)
    print(min_count)
