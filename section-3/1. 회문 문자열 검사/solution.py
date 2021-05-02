import sys

sys.stdin = open("in1.txt", "rt")

n = int(input())

for i in range(n):
    s = input()
    s = s.upper()
    size = len(s)

    # if s == s[::-1]: 거꾸로된 문자열
    for j in range(size // 2):
        if s[j] != s[-1 - j]:
            print("#%d NO" % (i + 1))
            break
    else:
        print("#%d YES" % (i + 1))
