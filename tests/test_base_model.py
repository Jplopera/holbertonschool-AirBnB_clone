#!/usr/bin/python3
"""Unittest for class BaseModel"""


import unittest
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    """Test Cases for the BaseModel class."""

    def test_save(self):
        """Test methot save"""
        b_1 = BaseModel()
        b_1.save()
        self.assertFalse(b_1.created_at == b_1.updated_at)

if __name__ == '__main__':
    unittest.main()
