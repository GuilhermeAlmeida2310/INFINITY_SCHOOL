class Animal:

    def talk(self):
        return f'The animal makes a generic sound.'

animal_ = Animal()

print(animal_.talk())

class Dog:

    def talk(self):
        return f'The dog is barking!'
    
dog_ = Dog()

print(dog_.talk())

class Cat:
    def talk(self):
        return f'The cat is meowing'
    
cat_ = Cat()

print(cat_.talk())