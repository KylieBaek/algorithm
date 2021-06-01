# 전역변수와 지역변수 리스트

def DFS():
    a[0] = 7  # 새로운 리스트(로컬 리스트)를 생성하는 것이 아님
    print(a)


def DFS2():
    a = [7, 8]  # 새로운 리스트(로컬 리스트) 생성
    print(a)


def DFS3():
    # a = a +[4] # ERROR 새로운 리스트(로컬 리스트) 생성했는데 초기값이 없어서 에러남

    global a
    a = a + [4]
    print(a)


if __name__ == "__main__":
    a = [1, 2, 3]
    DFS()
    DFS2()
    DFS3()

    print(a)

# [7, 2, 3]
# [7, 8]
# [7, 2, 3, 4]
# [7, 2, 3, 4]
