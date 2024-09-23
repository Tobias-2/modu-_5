class Car:
    def __init__(self, make, model_name, top_speed, color):
        self.make = make
        self.model_name = model_name
        self.top_speed = top_speed
        self.color = color
        # Variables
        self.current_speed = 0

    def accelerate(self, step=10):
        self.current_speed += step

    def decelerate(self, step=10):
        self.current_speed -= step

    def set_current_speed(self, value):
        if value <= self.top_speed:
            self.current_speed = value
        else:
            raise ValueError(f"Value {value} exceeds top speed of {self.top_speed}")

    def __str__(self):
        return f'{self.color} {self.make} {self.model_name}'


class Truck(Car):
    def __init__(self, max_load, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_load = max_load


# Creating car and truck objects
car = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")
truck = Truck(make="Mercedes", model_name="Actros", color="Black", top_speed=90, max_load=1200)

s = isinstance(car, Car)



class DieselEngine:
   def tank(self, how_many=100):
       print(f"Adding {how_many} liters of Diesel")

class PetrolEngine:
   def tank(self, how_many=20):
       print(f"Adding {how_many} liters of Petrol")

class Truck(Car, DieselEngine):

   def __init__(self, max_load, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.max_load = max_load

class SportCar(Car, PetrolEngine):
   pass


truck = Truck(make="Mercedes", model_name="Sprinter", color="Black", top_speed=90, max_load=1200)
porsche = SportCar(make="Porsche", model_name="911", color="Red", top_speed=250)
truck.tank()
porsche.tank()