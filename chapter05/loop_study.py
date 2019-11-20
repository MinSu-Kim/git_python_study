for i in [0, 1, 2, 3, 4, 5]:
    print(i, end=' ')

print()
for i in range(1, 10):
    print(i, end=" ")

print()
for i in range(0, 10, 2):
    print(i, end=' ')

print()
print("{} {}".format(range(10), list(range(10))))


# gugudan
def gugu(dan):
    for i in range(1, 10):
        print("{0} * {1} = {2:2}".format(dan, i, dan*i))


def gugudan():
    for dan in range(2, 10):
        print("\n=== {}단 ===".format(dan))
        gugu(dan)


def gugudan_land():
    for i in range(1, 10):
        for dan in range(2, 10):
            print("{0} * {1} = {2:2}".format(dan, i, dan*i), end='\t')
        print()

gugu(2)
gugudan()
gugudan_land()


"""
2 * 1 = 2   3 * 1 = 3 .... 9 * 1 = 9
2 * 2 = 4                  9 * 2 = 18
"""