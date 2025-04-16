class friend1:
    name = "" # attributes

    def person1(self):
        print("nice to see you guys")
class friend2:
    name = ""

    def person2(self):
        print("after a years")

class person(friend1,friend2):

    def people(self):
        print("I am happy to see you")

rubitha = person() # which OBJECT name is given that name only give to tha below functions
rubitha.person2() # bracket is must here for all oops program
rubitha.person1()
rubitha.people()

                         # ******* ANOTHER TYPE ********

class friend1:
    #name = "" # attributes
    def __init__(self):
        print("WELCOME FRIENDS")

    def person1(self,name):
        print(f"{name}: nice to see you guys")

class friend2:
    #name = "" # here it given or not given does not affect the program

    def person2(self,name):
        print(f"{name}:after a years we meted")

class person(friend1,friend2):

    def people(self,name):
        print(f"{name}:I am happy to see you guys")

rubitha = person() # which OBJECT name is given that name only give to tha below functions
rubitha.person2("rubitha") # bracket is must here
rubitha.person1("ramya")
rubitha.people("udhaya")
