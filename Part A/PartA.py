#main class

class Vehicle:

    def __init__(self, name, year, max_speed, mileage, colour):
        self.name = name
        self.year = year
        self.max_speed = max_speed
        self.mileage = mileage
        self.colour = colour

    # print attributes
    def print_attributes(self):
         print(f"Name: {self.name}")
         print(f"Year: {self.year}")
         print(f"Max Speed: {self.max_speed} km/h")
         print(f"Mileage: {self.mileage} km")
         print(f"Colour: {self.colour}")

    def update_name(self, name):
        if isinstance(name, str):
            self.name = name

    def update_year(self, year):
        if isinstance(year, int):
            self.year = year

    def update_max_speed(self, max_speed):
        if isinstance(max_speed, (int, float)):
            self.max_speed = max_speed 

    def update_mileage(self, mileage):
        if isinstance(mileage, (int, float)):
            self.mileage = mileage

    def update_colour(self, colour):
        if isinstance(colour, str):
            self.colour = colour

# Child class with attributes
class Car(Vehicle):

    def __init__(self, name, year, max_speed, mileage, colour, num_doors, engine_type):
        super().__init__(name, year, max_speed, mileage, colour)
        self.num_doors = num_doors
        self.engine_type = engine_type 

    def print_attributes(self):
        super().print_attributes()
        print(f"Number of Doors: {self.num_doors}")
        print(f"Engine Type: {self.engine_type}")  

    def update_num_doors(self, num_doors):
        if isinstance(num_doors, int):
            self.num_doors = num_doors

    def update_engine_type(self, engine_type):
        if isinstance(engine_type, str):
            self.engine_type = engine_type    

#  Create instances
v1 = Vehicle("Motorbike", 2020, 180, 15000, "Red")
c1 = Car("BMW", 2022, 220, 12000, "Blue", 4, "Petrol")

print("Initial Vehicle:")
v1.print_attributes()
print("\nInitial Car:")
c1.print_attributes()

v1.update_name("Scooter")
v1.update_colour("Black")

# Update 2 attributes in Car
c1.update_engine_type("Hybrid")
c1.update_num_doors(2)

print("\nUpdated Vehicle:")
v1.print_attributes()

print("\nUpdated Car;")
c1.print_attributes()


    


        