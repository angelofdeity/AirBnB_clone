#!/usr/bin/python3
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import unittest
from datetime import datetime
"""Tests the BaseModels"""


class TestBaseModel(unittest.TestCase):
    """Tests for BaseModel"""

    def setUp(self):
        """Sets up test methods"""
        self.b = BaseModel()

    def test_init(self):
        """Tests the creation of
        an instance of BaseModel"""
        b1 = BaseModel()
        self.assertIsInstance(b1, BaseModel)
        self.assertTrue(b1.id)
        self.assertTrue(b1.created_at)
        self.assertTrue(b1.updated_at)

    def test_id(self):
        """Tests the id of the BaseModel instance"""
        b1 = BaseModel()
        self.assertIsInstance(b1.id, str)
        self.assertEqual(len(b1.id), 36)

    def test_unique_id(self):
        """Test if id is unique"""
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_created_at(self):
        """Tests the created_at
        attribute of the BaseModel instance"""
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertIsInstance(b1.created_at, datetime)
        self.assertIsInstance(b2.created_at, datetime)
        self.assertNotEqual(b1.created_at, b2.created_at)

    def test_updated_at(self):
        """test updated_at"""
        self.assertIsInstance(self.b.updated_at, datetime)
        previous_update = self.b.created_at
        self.b.name = "betty"
        self.assertNotEqual(previous_update, self.b.updated_at)

    def test_kwargs(self):
        """test kwargs"""
        objdict = self.b.to_dict()
        b1 = BaseModel(**objdict)
        self.assertEqual(b1.id, self.b.id)
        self.assertIsNot(b1, self.b)

    def test___str__(self):
        """Test str method"""
        b1 = BaseModel()
        self.assertIsInstance(b1.__str__(), str)

    def test_save(self):
        """Tests the save method of
        the BaseModel instance"""
        b1 = BaseModel()
        # b1.id = 1
        b1.save()
        storage = FileStorage()
        obj = storage.all()
        key = f"{b1.__class__.__name__}.{b1.id}"

        self.assertIs(b1, obj[key])

    def test_to_dict(self):
        """Tests the to_dict method of the BaseModel instance"""
        bm_dict = self.b.to_dict()
        self.assertEqual(type(bm_dict), dict)
        self.assertEqual(bm_dict['__class__'], 'BaseModel')
        self.assertEqual(type(bm_dict['created_at']), str)
        self.assertEqual(type(bm_dict['updated_at']), str)
        self.assertEqual(bm_dict['id'], self.b.id)
        self.assertEqual(bm_dict['created_at'],
                         datetime.isoformat(self.b.created_at))
        self.assertEqual(bm_dict['updated_at'],
                         datetime.isoformat(self.b.updated_at))


if __name__ == '__main__':
    unittest.main()
