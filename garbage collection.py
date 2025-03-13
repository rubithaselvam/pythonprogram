import gc


class Demo:
    def __del__(self):
        print(f"Object {self} is bring destroyed")


def create_objects():
    obj1 = Demo()
    obj2 = Demo()

    # creating circular reference
    obj1.ref = obj2
    obj2.ref = obj1

    del obj1
    del obj2

    print("Running garbage collector....")
    gc.collect()


gc.disable()

create_objects()

gc.enable()
