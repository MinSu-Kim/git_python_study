def string_split():
    coffee_menu = "에스프레소 아메리카노 카페라떼 카푸치노"
    print(type(coffee_menu.split()))
    coffee_list = coffee_menu.split()
    [print(coffee) for coffee in coffee_list]
    print()
    coffee_menu2 = "에스프레소,아메리카노,카페라떼,카푸치노"
    [print(coffee) for coffee in coffee_menu2.split(',')]
    print()
    coffee_menu3 = "에스프레소\n아메리카노\n카페라떼\n카푸치노"
    [print(coffee) for coffee in coffee_menu3.split()]
    print()
    [print(coffee) for coffee in coffee_menu2.split(',', 2)]


def string_strip():
    python_str01 = "   Python    "
    python_str02 = "aaaPythonaa"
    python_str03 = "aabbPythonbbaaa"
    python_str04 = "aaaBallaaa"
    python_str05 = "\n This is very \n fast.\n\n"
    print(python_str01.strip())
    print(python_str02.strip('a'))
    print(python_str03.strip('ab'))
    print("중간에 공백은 제거 불가능", python_str04.strip('a'))
    print(python_str05.strip())


def string_concat():
    a = ","
    coffee_menu = "에스프레소 아메리카노 카페라떼 카푸치노".split()
    join_str = a.join(coffee_menu)
    print(type(join_str), join_str)


def string_find_count():
    str_f = "Python code Python"
    print(str_f.find("Python"))
    print(str_f.find("code"))
    print(str_f.rfind("Python"))

    str_f_se = "Python is powerful. Python is easy to learn"
    print(str_f_se.find("Python", 10, 30))
    print(str_f_se.find("Python", 35))

    print("Python의 개수는?", str_f_se.count("Python"))

    print(str_f.startswith('P'))
    print(str_f.endswith('n'))


def string_replace():
    str_b = '[Python]'
    print(str_b.replace('Python', 'IPython'))
    str_b = str_b.replace('[', '')
    str_b = str_b.replace(']', '')
    print(str_b)



if __name__ == "__main__":
    # string_split()
    # string_strip()
    # string_concat()
    # string_find_count()
    string_replace()