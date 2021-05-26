import sys

sys.stdin = open("in1.txt", "rt")

n1 = input()
n2 = input()

hash = dict()

for x in n1:
    hash[x] = hash.get(x, 0) + 1
for x in n2:
    hash[x] = hash.get(x, 0) - 1

for x in n1:
    if hash.get(x) != 0:
        print("NO")
        break
else:
    print("YES")
