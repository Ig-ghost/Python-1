#Polymorphism -> ability to take different forms

#gangadhar hi shaktiman hai
#peter parker is spiderman

# print(5 + 6)
# print('5' + '6') #concatenation
# print('nit' + ' ' + 'batch')

#polymorphism created by plus operator

#method overriding

class Person:
    def show(self):
        print('this is person')

class Emplopyee(Person):
    def show(self):
        print('this is employee')

a = Emplopyee()
# a.show()

b = Person()
# b.show()

class Parent:
    def __init__(self):
        self.value = 'Inside Parent'

    def show(self):
        print(self.value)

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.value = 'Inside Child'

    def show(self):
        print(self.value)

c = Parent()
d = Child()

# c.show()
# d.show()

#Abstraction -> hide irrrelavent details from user

print('hello world')

#abstract classes and abstract methods