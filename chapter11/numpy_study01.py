import numpy as np


def seq_array():
    data1 = list(range(0,10));
    print(type(data1), data1)
    a1 = np.array(data1)
    print(type(a1), a1.dtype, a1)

    data2 = [0.1, 5, 4, 12, 0.5]
    a2 = np.array(data2)
    print(a2.dtype, a2)


def two_dimension_array():
    a3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(a3.dtype, a3, a3.shape)
    print(a3.shape)


def range_array():
    print("np.arange(0, 10, 2) : ", np.arange(0, 10, 2))
    print("np.arange(1, 10) : ", np.arange(1, 10))
    print("np.arange(5) : ", np.arange(5))

    b1 = np.arange(12).reshape(4,3)
    print("b1.shape : ",  b1.shape)
    print("np.arange(12).reshape(4,3) : ", b1)

    print("np.arange(5) : {}\nnp.arange(5).shape : {} ".format(np.arange(5), np.arange(5).shape))


def num_array():
    print("==num_array==")
    n1 = np.linspace(1, 10, 5)
    print("np.linspace(1, 10, 5) : {} dtype : {}".format(n1, n1.dtype, n1))
    n2 = np.linspace(0, np.pi, 20)
    print("np.linspace(0, np.pi, 20) : {} dtype : {}".format(n2, n2.dtype, n2))
    print(np.zeros(5))
    print(np.zeros((3,4)))
    print(np.ones(5))
    print(np.ones((3,4)))
    print(np.eye(4))


def type_conversion():
    str_array = np.array(['1.5', '0.62', '2', '3.14', '3.141592'])
    print(str_array, str_array.dtype)
    float_array = str_array.astype(float)
    print(float_array, float_array.dtype)


def rand_array():
    np.random.seed(1)
    rnd01 = np.random.rand(2, 3)
    print(rnd01.dtype, rnd01)
    print()
    print(np.random.rand())
    print(np.random.rand(2, 3, 4))
    print(np.random.randint(10, size=(2,3)))
    print(np.random.randint(30))


def array_expression():
    arr1 = np.array(range(10, 50, 10))
    arr2 = np.array(range(1, 5))

    print("arr1 = {} \narr2 = {}".format(arr1, arr2))

    arr3 = arr1 + arr2
    print("arr1 + arr2 = {}".format(arr3))

    arr4 = arr1 - arr2
    print("arr1 - arr2 = {}".format(arr4))

    arr5 = arr2 * 2
    print("arr2 * 2 = {}".format(arr5))

    arr6 = arr2 ** 2
    print("arr2 ** 2 = {}".format(arr6))

    arr7 = arr1 * arr2
    print("arr1 * arr2 = {}".format(arr7))

    arr8 = arr1/arr2
    print("arr1 / arr2 = {}".format(arr8))

    arr9 = arr1 / (arr2 ** 2)
    print("arr1 / (arr2 ** 2) = {}".format(arr9))

    print("arr1 = {}, arr1>20 = {}".format(arr1, arr1>20))


def stat_expression():
    arr = np.arange(1,6)
    print("arr = {}\n"
          "sum()={} mean()={}, std()={}, var()={}, min={}, max()={}, "
          "cumsum()={}, cumprod()={}".
          format(arr, arr.sum(), arr.mean(), arr.std(), arr.var(), arr.min(),
                 arr.max(), arr.cumsum(), arr.cumprod()))


def matrix_ex():
    a = np.array(range(4)).reshape(2,2)
    print(a)
    b = np.array([3, 2, 0, 1]).reshape(2,2)
    print(b)

    print("a.dot(b) = \n{}\nnp.dot(a,b) \n= {}".format(a.dot(b), np.dot(a, b)))
    print("np.transpose(a) \n {}".format(np.transpose(a)))
    print("a\n{}\n역행렬\n{}\n행렬식 {}".format(a, np.linalg.inv(a), np.linalg.det(a)))


if __name__ == "__main__":
    # seq_array()
    # two_dimension_array()
    # range_array()
    # num_array()
    # type_conversion()
    # rand_array()
    # array_expression()
    # stat_expression()
    matrix_ex()