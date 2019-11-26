file_name = "coffeeShopSales.txt"

with open(file_name, "r") as f:
    for line in f:
        print(line, end='')

with open(file_name, "r") as f:
    header = f.readline()
    print(header, header.split())
    header_list = header.split()
    coffee_list =[]
    [coffee_list.append(line.split()) for line in f]
    data_list=[]
    for i in range(len(coffee_list)):
        data_dict = {}
        for head, value in zip(header_list, coffee_list[i]):
            print(head, value)
            data_dict[str(head)]=value
        data_list.append(data_dict)

    [print(type(data), data) for data in data_list]


