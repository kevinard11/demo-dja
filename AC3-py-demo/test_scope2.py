from random import shuffle


class Dog():
    name: str

    def __init__(self,breed=1, name=2) -> None:
        self.breed = breed
        self.name = name

    def setRadius(self, new_radius):
        self.radius = new_radius
        self.area = new_radius * new_radius * self.pi

myDog = Dog('Lab')
myDog.name = 'test'
myDog.breed = 'testtt'
print(myDog.breed)
print(myDog.name)


cards = [('h','2'),('a','2'),('b','3'),('c','5')]
print(cards)
shuffle(cards)
print(cards)
split = (cards[:2], cards[2:])
print(split)