## Inheritance
## Class A - is parent class
## Class B - is child class which inherits features from parent class A

class ParentClass:
    def __init__(self, name):
        self.name = name

    def diplay_names(self):
        print(self.name)

class ChildClass(ParentClass):
    def __init__(self, name):
        super().__init__(name)
        self.age = 20

    def change_name(self, name):
        self.name = name

    def display_age(self):
        print(self.age)

child_obj = ChildClass("Sachin")
child_obj.diplay_names()
child_obj.change_name("Virat")
child_obj.diplay_names()
child_obj.display_age()