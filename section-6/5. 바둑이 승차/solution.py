import sys

sys.stdin = open("in1.txt", "rt")


# 부분집합 합 최대 (시간 초과 Cut Edge tech)
def DFS(L, sum, current_sum):
    # L =  index of a
    global max_sum
    if sum + (total - current_sum) < max_sum:
        return
    if sum > c:
        return

    if L == n:
        if max_sum < sum:
            max_sum = sum
        return

    DFS(L + 1, sum + a[L], current_sum + a[L])
    DFS(L + 1, sum, current_sum + a[L])


if __name__ == "__main__":
    c, n = map(int, input().split())
    a = list()
    max_sum = -2147000000

    for _ in range(n):
        a.append(int(input()))
    total = sum(a)

    DFS(0, 0, 0)
    print(max_sum)
