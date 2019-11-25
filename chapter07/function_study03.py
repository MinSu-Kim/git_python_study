a = 5  # 전역 변수


def func1():
    a = 1  # 지역 변수. func1()에서만 사용
    print("[func1] 지역 변수 a =", a)


def func2():
    a = 2  # 지역 변수. func2()에서만 사용
    print("[func2] 지역 변수 a =", a)


def func3():
    print("[func3] 전역 변수 a =", a)


def func4():
    global a  # 함수 내에서 전역 변수 변경 위해 선언
    a = 4  # 전역 변수의 값 변경
    print("[func4] 전역 변수 a =", a)


def anony(x):
    return x ** 2


if __name__ == "__main__":
    res = (lambda x: x ** 2)(3)

    mySquare = lambda x: x ** 2
    print(mySquare(9))
    print(res)

    list1 = [1, 2, 3, 4, 5]
    # ==> 1, 4, 9, 16, 25
    # 홀수의 경우만 1, 9, 25
    for i in list1:
        if i % 2 == 1:
            print(i ** 2, end=' ')

    print()
    [print(i ** 2, end=' ') for i in list1 if i % 2 == 1]
