class Vehicle:
    def move(self): 
        print("Moving on the road")

class Car(Vehicle):
    def move(self):
        print("Driving on the road")

class Bicycle(Vehicle):
    def move(self): 
        print("Pedaling on the road")

def start_journey(vehicle):
    # This works because both objects share the move() interface
    vehicle.move()

# Creating instances
my_car = Car()
my_bike = Bicycle()

# Polymorphism in action
start_journey(my_car)  # Output: Driving on the road
start_journey(my_bike) # Output: Pedaling on the road
