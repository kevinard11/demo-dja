print(" Class")
class Sample:
    pass
x = Sample()

print(type(x)) #<class '__main__.Sample'>

print("\n Class with attribute")
class Dog:
    def __init__(self,breed):
        self.breed = breed
        
sam = Dog(breed='Lab')
print(sam.breed) #Lab

print("\n Class with object attribute")
class Dog:
    species = 'mammal'
    
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name
sam = Dog('Lab','Sam')
print(sam.species) #mammal

print("\n Class with methods")
class Circle:
    pi = 3.14
    def __init__(self, radius=1):
        self.radius = radius 
        self.area = radius * radius * Circle.pi

    def setRadius(self, new_radius):
        self.radius = new_radius
        self.area = new_radius * new_radius * self.pi

    def getCircumference(self):
        return self.radius * self.pi * 2

c = Circle()
print('Radius is: ',c.radius) #Radius is:  1
print('Area is: ',c.area) #Area is:  3.14
print('Circumference is: ',c.getCircumference()) #Circumference is:  6.28

print("\n Class with inheritance")
class Animal:
    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def whoAmI(self):
        print("Dog")

    def bark(self):
        print("Woof!")

d = Dog() #Animal created
          #Dog created
d.whoAmI() #Dog
d.eat() #Eating
d.bark() #Woof!

print("\n Class with polymorphism")
class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name+' says Woof!'
    
class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name+' says Meow!'     
niko = Dog('Niko')
felix = Cat('Felix')
print(niko.speak()) #Niko says Woof!
print(felix.speak()) #Felix says Meow!

class Animal:
    def __init__(self, name):    # Constructor of the class
        self.name = name

    def speak(self):              # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    
    def speak(self):
        return self.name+' says Woof!'
    
class Cat(Animal):

    def speak(self):
        return self.name+' says Meow!'
fido = Dog('Fido')
isis = Cat('Isaac')
print(fido.speak()) #Fido says Woof!
print(isis.speak()) #Isaac says Meow 

print("\n Class with special method")
class Book:
    def __init__(self, title, author, pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: %s, author: %s, pages: %s" %(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book is destroyed")
book = Book("Python Rocks!", "Jose Portilla", 159)
print(book) # (__str__) A book is created
print(len(book)) #(__len__) 159
del book #(__del__) A book is destroyed
# print(book) #fail, because book is already destroyed, have to create book object again