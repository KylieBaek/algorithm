import sys

sys.stdin = open("in1.txt", "rt")
s = input()
res = 0
cnt = 0

for x in s:
    if x.isdecimal():  # 0 ~ 9
        res = res * 10 + int(x)

# 약수 개수
for i in range(1, res + 1):
    if res % i == 0:
        cnt += 1

print(res)
print(cnt)
