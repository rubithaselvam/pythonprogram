class student: # class created
    def __init__(self,name,mark): # constructor created
        self.name = name
        self.__mark = mark
        self.__old_mark = mark

    def get_mark(self):
        return self.__mark

    def set_mark(self,new_mark):
        if 0 <= new_mark <= 100:
            self.__old_mark = self.__mark
            self.__mark = new_mark
        else:
            print("Incorrect mark range. The range is 0 to 100")

    def get_old_mark(self):
        return self.__old_mark

student1 = student("john", 79)
student1.set_mark(87)

print(f"{student1.name}, old mark: {student1.get_old_mark()}, updated mark: {student1.get_mark()}")



