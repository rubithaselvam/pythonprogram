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


