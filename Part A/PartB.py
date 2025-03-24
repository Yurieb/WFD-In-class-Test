import unittest
from PartA import Vehicle, Car

class TestVehicleAndCar(unittest.TestCase):

    # Check if objects are instances of classes
    def setUp(self):
        self.v1 = Vehicle("Motorbike", 2018, 160, 23000, "Green")
        self.car1 = Car("Toyota Corolla", 2020, 180, 15000, "Silver", 4, "Petrol")
        self.car2 = Car("Tesla Model 3", 2023, 200, 5000, "White", 4, "Electric")
        self.car3 = self.car1  # Same object as car1

    def test_incstance_of_class(self):
        self.assertIsInstance(self.v1, Vehicle)
        self.assertIsInstance(self.car1, Car)
        self.assertIsInstance(self.car2, Vehicle)

    def test_not_instance_of_class(self):
        self.assertNotIsInstance(self.v1, Car)
        self.assertNotIsInstance("Nissan", Vehicle) 

    def test_object_identity(self):
        self.assertIs(self.car1, self.car3)   # Same object
        self.assertIsNot(self.car1, self.car2)  

    def test_update_methods(self):
        self.v1.update_name("Ducati Monster")
        self.v1.update_colour("Red")
        self.assertEqual(self.v1.name, "Ducati Monster")
        self.assertEqual(self.v1.colour, "Red")

        self.car1.update_engine_type("Hybrid")
        self.car1.update_num_doors(2)
        self.assertEqual(self.car1.engine_type, "Hybrid")
        self.assertEqual(self.car1.num_doors, 2)
             
if __name__ == '__main__':
    unittest.main()
