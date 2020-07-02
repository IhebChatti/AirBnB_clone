#!/usr/bin/python3
"""
    TestFileStorage module
"""
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
        TestFileStorage class
    """

    def test_instance_storage_form_FileStorage(self):
        """
            Test
        """
        self.assertIsInstance(storage, FileStorage)

    def test_objects_should_be_dictionary(self):
        """
            Test
        """
        s = storage.all()
        self.assertIsInstance(s, dict)

    def test_file_path_instance(self):
        """
        Test raise error
        """
        with self.assertRaises(AttributeError):
            f = FileStorage.__file_path

    def test_objects_instance(self):
        """
        Test raise error
        """
        with self.assertRaises(AttributeError):
            f = FileStorage.__objects

    def test_all_method(self):
        """
        Test all method
        """
        d = storage.all()
        self.assertIsInstance(d, dict)

    def test_new_method(self):
        """
        Test new method
        """
        l = storage.all()
        obj = BaseModel()
        storage.new(obj)
        ll = storage.all()
        self.assertEqual(len(l), len(ll))
