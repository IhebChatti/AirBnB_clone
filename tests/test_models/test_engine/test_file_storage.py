#!/usr/bin/python3
"""
    TestFileStorage module
"""
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from models.engine.file_storage import FileStorage


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
