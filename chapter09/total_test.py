file_name = "coffeeShopSales.txt"

with open(file_name, "r") as f:
    header = f.readline()
    header_list = header.split()
    coffee_list =[]
    [coffee_list.append(line.split()) for line in f]
    data_list=[]
    for i in range(len(coffee_list)):
        data_dict = {}
        for head, value in zip(header_list, coffee_list[i]):
            data_dict[str(head)]=float(value)
        data_list.append(data_dict)

    [print(data) for data in data_list]

    result = {}
    stat = {}
    for coffee in data_list:
        for k in coffee.keys():
            if k != '날짜':
                result[k] = result.get(k, 0) + int(coffee[k])  # 없을때의 리턴값을 정해 줌
                stat[k] = stat.get(k, 0) + 1

    print()
    for p, c in zip(result.keys(), stat.keys()):
        print("{} 판매량 {}, 하루 평균{:.2f}".format(p, result[p], result[p]/stat[c]))



