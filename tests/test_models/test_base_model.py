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

if __name__ == '__main__':
    unittest.main()
