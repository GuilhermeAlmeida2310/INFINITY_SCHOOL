class Vehicle:
    def to_move(self):
        return 'The vehicle is in motion!'
    
class Car(Vehicle):
    def to_move(self):
        return 'The car is in motion!'

class Motorcycle(Vehicle):
    def to_move(self):
        return 'The motorcycle is in motion!'

vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

print(vehicle.to_move())
print(car.to_move())
print(motorcycle.to_move())