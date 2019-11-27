import random

def rand_int():
    dice1 = random.randint(1,6) # 임의의 정수가 생성됨
    dice2 = random.randint(1,6) # 임의의 정수가 생성됨
    print('주사위 두 개의 숫자: {0}, {1}'.format(dice1, dice2))


def rand_range():
    num1 = random.randrange(1, 10, 2)  # 1 ~ 9(10-1) 중 임의의 홀수 선택
    num2 = random.randrange(0, 100, 10)  # 0 ~ 99(100-1) 중 임의의10의 단위 숫자 선택
    print('num1: {0}, num2: {1}'.format(num1, num2))


def rand_choice():
    menu = ['비빔밥', '된장찌개', '볶음밥', '불고기', '스파게티', '피자', '탕수육']
    print("choice(menu) {}". format(random.choice(menu)))


def rand_sample():
    random.sample([1, 2, 3, 4, 5], 2)  # 모집단에서 두 개의 인자 선택
    print("random.sample([1, 2, 3, 4, 5], 2) => {}".format(random.sample([1, 2, 3, 4, 5], 2)))


if __name__ == "__main__":
    rand_int()
    rand_range()
    rand_choice()
    rand_sample()