#magic methods/ dunder methods --> starts and ends with double underscores

#generally used for operator overloading

# print(dir(int))

class String:
    def __init__(self, string):#magic method
        self.string = string

#driver code

string1 = String('hello')

# print(string1)

# 2. __repr__ method

class New:
    def __init__(self, string):
        self.string = string

    #to print our string object
    def __repr__(self):
        return 'object : {}'.format(self.string)
    
string2 = New('hello')
# print(string2 + 'world')

#__add__ method

class This:
    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return 'Object : {}'.format(self.string)
    
    def __add__(self, other):
        return self.string + other
    
newthis = This('hello')
# print(newthis + 'world')

#operator overloading -> giving extended meaning beyond its predefined meaning

# print(1 + 2)
# print('1' + '2')

# print(3 * 4)
# print('hey' * 4)   


#overloading add operator

class A:
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        return self.a + other.a
    
# obj1 = A(1)
# obj2 = A(20)

# obj3 = A('hello')
# obj4 = A('world')

# print(obj1 + obj2)
# print(obj3 + obj4)

# print(A.__add__(obj1, obj2))
# print(A.__add__(obj3, obj4))

# print(obj1.__add__(obj2))
# print(obj3.__add__(obj4))

#adding two complex numbers using add

class complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return self.a + other.a, self.b + other.b

obj1 = complex(1, 2)
obj2 = complex(3, 4)
obj3 = obj1 + obj2
print(obj3)

#output -> (4, 6)

#__str__ --> string representation of an object

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Name : {self.name}, Age : {self.age}'
    
newPerson = Person('Devansh', 20)
print(newPerson)

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price= price

    def __str__(self):
        return f'{self.title} by {self.author} priced at Rs{self.price}'
    
newBook = Book('Python Programming', 'Myself', 2000)
print(newBook)

#python completed