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