class Bicycle():

    def __init__(self, wheel_size=10, color='white'):
        self.wheel_size = wheel_size
        self.color = color

    def move(self, speed):
        print("자전거: 시속{}킬로미터로 전진".format(speed))

    def turn(self, direction):
        print("자전거 : {}회전".format(direction))

    def stop(self):
        print("자전거({}, {}): 정지".format(self.wheel_size, self.color))

    def __str__(self) -> str:
        return str("자전거({}, {})".format(self.wheel_size, self.color))


class Car(Bicycle):
    def stop(self):
        print("자동차({}, {}): 정지".format(self.wheel_size, self.color))


if __name__ == "__main__":
    my_bicyle = Bicycle()

    my_bicyle2 = Bicycle(30, "black")

    [print(c) for c in [my_bicyle, my_bicyle2]]

    print(my_bicyle.wheel_size)