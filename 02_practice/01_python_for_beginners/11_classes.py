# ----------------------------------- Basics ----------------------------------- #
# All objects are instances of a class. A class is like an object constructor, or a "blueprint" for creating objects.


class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def greet(self):
        print(f"My name is {self.lname}. {self.fname} {self.lname}")


double_o_seven = Person(
    "James", "Bond"
)  # double_o_seven is now an instance of a person
double_o_seven.greet()


# -------------------------------- Inheritance -------------------------------- #


class Scientist(Person):
    def __init__(self, fname, lname, expertise):
        super().__init__(fname, lname)  # inheriting this from the parent class
        self.expertise = expertise

    def tell_expertise(self):
        print(f"My expertise is {self.expertise}")


ibrahim = Scientist(fname="Ibrahim", lname="Kocyigit", expertise="Machine Learning")
ibrahim.greet()  # This method was automatically inherited. -> My name is Kocyigit. Ibrahim Kocyigit
ibrahim.tell_expertise()  # -> My expertise is Machine Learning
