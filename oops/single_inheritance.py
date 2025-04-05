class relations: # BASE CLASS
    name = ""

    def hii(self):
        print("hello relatives")

class guest(relations): # DERIVED CLASS

    def hii(self):
        super().hii() # super class is used to call the function in BASE CLASS print function

        print("welcome to the function")

abi = guest() # object creating for derived class. that the object is used for all the function to call
abi.hii()

