#!/usr/bin/python3
"""Unittest for class FileStorage"""


import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import datetime
import models
import os


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """
        """
        self.object_test = BaseModel()

    def reset_Storage(self):
        """
        """
        FileStorage.__objects = {}
        if os.path.exists(FileStorage.__file_path):
            os.remove(FileStorage.__file_path)

    def tearDown(self):
        """
        """
        self.reset_Storage()
        pass

    def test_attributes(self):
        """
        """
        self.reset_Storage()
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        self.assertEqual(getattr(FileStorage, "_FileStorage__objects"), {})

    def test_all_base_model(self):
        """Tests all() method for BaseModel."""
        self.check_all("BaseModel")

    def test_new_base_model(self):
        """Tests new() method for BaseModel."""
        self.check_new("BaseModel")

    def test_save_base_model(self):
        """Tests save() method for BaseModel."""
        self.check_save("BaseModel")

    def test_reload_base_model(self):
        """Tests reload() method for BaseModel."""
        self.check_reload("BaseModel")

if __name__ == "__main__":
    unittest.main()