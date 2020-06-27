#!/usr/bin/python3
"""
    FileStorage modul
"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):

    def test_public_class_attribute_assignemet_for_file_path(self):
        fs = FileStorage()
        f = FileStorage._FileStorage__file_path
        self.assertEqual(f, "file.json")

    def test_public_class_attribute_assignemet_for_objs(self):
        fs = FileStorage()
        o = FileStorage._FileStorage__objects
        self.assertEqual(o, {})

    def test_all_instance_method_returns(self):
        fs = FileStorage()
        dct = fs.all()
        self.assertEqual(dct, {})

    def test_new_instance_method(self):
        fs = FileStorage()
        obj = BaseModel()
        _id = "BaseModel" + "." + obj.id
        fs.new(obj)
        o = FileStorage._FileStorage__objects
        self.assertEqual(o[obj], _id)
