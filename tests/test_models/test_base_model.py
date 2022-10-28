#!/usr/bin/python3
"""Unittest for class BaseModel"""


import unittest
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    """Test Cases for the BaseModel class."""

    def test_save(self):
        """Test method save"""

        b1 = BaseModel()
        b1.save()
        self.assertFalse(b1.created_at == b1.updated_at)

    def test_dic(self):
        """Test method to_dic"""

        b1 = BaseModel()
        b1.name = "Juan"
        b2 = b1.to_dict()
        self.assertEqual(b2["name"], b1.name)

if __name__ == '__main__':
    unittest.main()
