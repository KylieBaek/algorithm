import sys

# 그리디 -> 정렬 후 선택
sys.stdin = open("in1.txt", "rt")

# 가장 높은 곳과 낮은 곳 차이 출력
L = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)

m = int(input())
for _ in range(m):
    # 그리디 - 가장 큰거 가장 작은거만 선택
    a[0] = a[0] - 1
    a[L - 1] = a[L - 1] + 1
    a.sort(reverse=True)  # 시간 초과 남

print(a[0] - a[L - 1])

# Solution 2 리스트 해쉬
# L=int(input())
# arr=list(map(int, input().split()))
# m=int(input())
# cnt=[0]*101
# maxH=float('-inf')
# minH=float('inf')
# for x in arr:
#     cnt[x]+=1
#     if x>maxH: maxH=x
#     if x<minH: minH=x
#
# for _ in range(m):
#     if cnt[maxH]==1:
#         cnt[maxH]-=1
#         maxH-=1
#         cnt[maxH]+=1
#     else:
#         cnt[maxH]-=1
#         cnt[maxH-1]+=1
#
#     if cnt[minH]==1:
#         cnt[minH]-=1
#         minH+=1
#         cnt[minH]+=1
#     else:
#         cnt[minH]-=1
#         cnt[minH+1]+=1
#
# print(maxH-minH)
