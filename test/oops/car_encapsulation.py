class car:
    def __init__(self):
        self.__speed = 0

    def set_speed(self,speed):
        if speed > 0:
            self.__speed = speed
        else:
            print("the speed can not be negative")

    def get_speed(self):
        return self.__speed

cars = car()
cars.set_speed(40)
cars.set_speed(-48)
print("current speed: ", cars.get_speed())
