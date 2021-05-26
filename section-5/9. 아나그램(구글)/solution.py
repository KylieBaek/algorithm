import sys

sys.stdin = open("in1.txt", "rt")

n1 = input()
n2 = input()

hash1 = dict()
hash2 = dict()

for x in n1:
    hash1[x] = hash1.get(x, 0) + 1 # key값 없으면 0 가져옴
for x in n2:
    hash2[x] = hash2.get(x, 0) + 1

for key in hash1.keys():
    if key in hash2.keys():
        if hash1[key] != hash2[key]:
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")
