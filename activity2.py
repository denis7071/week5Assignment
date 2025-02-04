from abc import ABC, abstractmethod

class Vehicle(ABC):
    """Abstract base class for all vehicles"""
    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Driving on the road 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying through the sky ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing on water ⛵")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling on bike paths 🚲")

class Rocket(Vehicle):
    def move(self):
        print("Blasting into space 🚀")

# Usage example
if __name__ == "__main__":
    # Create different vehicle instances
    vehicles = [
        Car(),
        Plane(),
        Boat(),
        Bicycle(),
        Rocket()
    ]

    # Demonstrate polymorphic behavior
    print("Vehicle Movement Simulation:")
    for index, vehicle in enumerate(vehicles, 1):
        print(f"\nVehicle {index}: ", end="")
        vehicle.move()

    # Individual usage example
    print("\nSpecialized Movement:")
    tesla = Car()
    boeing = Plane()
    kayak = Boat()

    tesla.move()    # Output: Driving on the road 🚗
    boeing.move()   # Output: Flying through the sky ✈️
    kayak.move()    # Output: Sailing on water ⛵