file_path = 'two_times_table.txt'


def file_write():
    global file_path
    print('===', file_write.__name__, '===')
    try:
        f = open(file_path, 'w')
        for num in range(1, 10):
            f.write("2 * {} = {}\n".format(num, num*2))
    except Exception as e:
        print(e)
    finally:
        f.close()
    print("{} file created ".format(file_path))


def file_read_line():
    global file_path
    print('===', file_read_line.__name__, '===')
    try:
        f = open(file_path, 'r')
        line = f.readline()
        while line:
            print(line, end="")
            line = f.readline()
    except FileNotFoundError as e:
        print("해당 파일이 존재하지 않음", e, sep='\n')
    finally:
        f.close()


def file_read_lines():
    global file_path
    print('===', file_read_lines.__name__, '===')
    try:
        f = open(file_path, 'r')
        lines = f.readlines()
        for line in lines:
            print(line, end="")
    except FileNotFoundError as e:
        print("해당 파일이 존재하지 않음", e, sep='\n')
    finally:
        f.close()


def file_read_object():
    global file_path
    print('===', file_read_object.__name__, '===')
    try:
        f = open(file_path, 'r')
        for line in f:
            print(line, end="")
    except FileNotFoundError as e:
        print("해당 파일이 존재하지 않음", e, sep='\n')
    finally:
        f.close()


def with_fileio():
    global file_path
    print('===', with_fileio.__name__, '===')
    try:
        with open(file_path, 'r') as f:
            for line in f:
                print(line, end="")
    except FileNotFoundError as e:
        print("해당 파일이 존재하지 않음", e, sep='\n')


# 4개의 함수를 정의


if __name__ == "__main__":

    file_write()
    file_read_line()
    file_read_lines()
    file_read_object()
    with_fileio()