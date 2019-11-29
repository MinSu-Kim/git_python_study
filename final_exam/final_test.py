# exam01
def exam01():
    with open("Gettysburg_Address.txt", 'r', encoding='utf-8') as f:
        try:
            f = open("Gettysburg_Address.txt", 'r')
            f.readline()
            data = f.read()
            # print(data)
            data = data.split()

            word_list = []
            [word_list.append(word.strip('.').strip(',').strip('-')) for word in data if len(word.strip('-')) > 0]
            # [print(data, end=' ') for data in word_list]

            # print()
            result = {}
            for word in word_list:
                result[word] = result.get(word, 0) + 1  # 없을때의 리턴값을 정해 줌

            # [print(key, value) for key,value in result.items() if value > 2]
            res = sorted(result.items(), key=f1, reverse=True)

            print("=== 문제1 ===")
            [print("{:10s}\t{}".format(key, value)) for key, value in res if value > 2]
            print()
        except FileNotFoundError as e:
            print("해당 파일이 존재하지 않음", e, sep='\n')


def f1(x):
    return x[1]


# exam02

func = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: x / y]
menu_list = ["더하기", "빼기", "곱하기", "나누기"]


def show_menu():
    for i, v in enumerate(menu_list):
        print("{}. {}".format(i, v))
    print("{}. {}".format(4, '종료'))
    return input("메뉴를 선택하세요.")


def exam02():
    while True:
        sel = int(show_menu())
        print()
        if sel < 0 or sel > len(func):
            continue
        if sel == len(func):
            print("프로그램을 종료합니다.")
            break
        x = input("첫번째 수 :")
        y = input("두번째 수 : ")
        print("연산 결과 = {}".format(func[sel](int(x), int(y))), end='\n\n')


# exam03

def exam03():
    cnt = 0
    while cnt < 10:
        cnt = cnt + 1
        print("나무꾼이 나무를 {}번 찍습니다.".format(cnt))
    print("나무가 넘어갑니다.")


# exam04

def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        answer.append(list(sorted(array[i - 1:j]))[k - 1])
    return answer


def exam04():
    array = [1, 5, 2, 6, 3, 7, 4]
    commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    answer = solution(array, commands)
    print(answer)


if __name__ == "__main__":
    exam01()
    exam02()
    exam03()
    exam04()
