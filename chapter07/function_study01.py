# def my_student_info(1. 리스트로전달, 2. 투플, 3, dictionary):


def my_student_info_list(std_list):
    for item in std_list:
        print("학생 이름 : {}\n학급 번호 : {}\n전화 번호 : {}\n"
              .format(item[0], item[1], item[2]))


def my_student_info_tuple(std_tuple):
    for item in std_tuple:
        print("학생 이름 : {}\n학급 번호 : {}\n전화 번호 : {}\n"
              .format(item[0], item[1], item[2]))


def my_student_info_dict(std_dict):
    for keys, values in std_dict.items():
        print("번호 {}".format(keys))
        for key, value in values.items():
            print("{} : {}".format(key, value))


if __name__ == "__main__":
    std_list = [["현아", "01", "01-235-6789"], ["진수", "02", "01-987-6543"]]
    my_student_info_list(std_list)

    std_tuple = (("현아", "01", "01-235-6789"), ("진수", "02", "01-987-6543"))
    my_student_info_tuple(std_tuple)

    std_dict = {"01": {"학생 이름": "현아", "학급 번호": "01", "전화 번호": "01-235-6789"},
                "02": {"학생 이름": "진수", "학급 번호": "02", "전화 번호": "01-987-6543"}}
    my_student_info_dict(std_dict)









