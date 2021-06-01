def DFS1():
    # 함수안에서 모든 변수는 지역변수 확인 후 전역변수 확인한다.
    cnt = 3  # 이 cnt는 지역변수 (전역변수보다 우선함)
    print(cnt)  # 3 출력


def DFS2():
    global cnt  # cnt는 전역변수다.
    if cnt == 5:
        cnt = cnt + 1  # 위의 global 없으면 로컬변수로 선언됨
        print(cnt)


if __name__ == "__main__":
    cnt = 5
    DFS1()
    DFS2()
    print(cnt)

# 3
# 6
# 6
