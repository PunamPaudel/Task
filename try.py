# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def bark(self):

#         print(self.name + " says woof")
#         print(f"{self.name} {self.age}")


# d1 = Dog("buddy", 3)
# d1.bark()
# d2 = Dog("tummy", 7)
# print(d2.bark())

# Inheritance

class Person:
    def __init__(self, firstname, lastname):
        self.fristname = firstname
        self.lastname = lastname


class Student(Person):
    pass


x = Student("Poonam", "Paudel")
print(x.fristname, x.lastname)


# super_class

class Boys(Person):
    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)


p1 = Person("Punam", "Paudel")
print(p1.fristname, p1.lastname)
