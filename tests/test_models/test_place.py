import unittest
import os
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """creates class"""
        cls.testCity = City()
        cls.testCity.name = "City Name"
        cls.testCity.state_id = "State ID"

    @classmethod
    def tearDownClass(cls):
        """deletes test class"""
        del cls.testCity
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_init_and_class_variables(self):
        """tests init and class variables"""
        self.assertTrue(isinstance(self.testCity, City))
        self.assertTrue(issubclass(type(self.testCity), BaseModel))
        self.assertTrue('name' in self.testCity.__dict__)
        self.assertTrue('state_id' in self.testCity.__dict__)
        self.assertTrue('id' in self.testCity.__dict__)
        self.assertTrue('created_at' in self.testCity.__dict__)
        self.assertTrue('updated_at' in self.testCity.__dict__)

    def test_save(self):
        self.testCity.save()
        self.assertTrue(self.testCity.updated_at != self.testCity.created_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.testCity), True)


if __name__ == '__main__':
    unittest.main()
