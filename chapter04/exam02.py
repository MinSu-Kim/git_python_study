import random as rnd


def swap(random_list, i, j):
    random_list[i], random_list[j] = random_list[j], random_list[i]
    return random_list

def bubble_sort(random_list):
    for cnt in range(len(random_list)-1):
        for i in range(len(random_list)-1):
            if random_list[i] > random_list[i+1]:
                # random_list[i], random_list[i+1] = random_list[i+1], random_list[i]
                random_list = swap(random_list, i, i+1)
        print("bubble_sort(random_list) => {}".format(random_list))
    return random_list


if __name__ == "__main__":
    random_list = []
    rnd.seed(1)
    for num in range(0, 10):
        random_list.append(rnd.randint(1, 46))
    print(random_list)

    sorted_list = bubble_sort(random_list)
    print("정렬된 결과 {}".format(sorted_list))