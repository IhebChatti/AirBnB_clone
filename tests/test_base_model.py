#!/usr/bin/python3
"""
    Test BaseModel module
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
        Tests base model class
    """

    def test_instance_creation_of_base_model(self):
        """
            Tests instance creation of the base model
        """
        bm = BaseModel()
        self.assertIsInstance(bm, BaseModel)

    def test_initilazes_base_model_instance_with_id(self):
        """
            Tests id assignment for a new instance
        """
        bm = BaseModel()
        uuid_pattern='[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}'
        self.assertRegex(bm.id, uuid_pattern)

    def test_avoid_id_duplication_for_instance(self):
        """
            Tests avoid ID duplications
        """
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_assignment_of_created_at_attribute(self):
        """"
            Tests created_at attribute
        """
        bm = BaseModel()
        c_at = bm.created_at
        self.assertIsInstance(c_at, datetime)

    def test_date_format_for_created_at(self):
        """
            Tests date format for datetime attribute
        """
        bm = BaseModel()
        c_at = bm.created_at.__str__()
        c_at_pattern='\d{4}\-\d{2}\-\d{2}\ \d{2}\:\d{2}\:\d{2}\.\d{6}'
        self.assertRegex(c_at, c_at_pattern)

    def test_assignment_of_updated_at_attribute(self):
        """
            Tests updated_at attribute
        """
        bm = BaseModel()
        u_at = bm.updated_at
        self.assertIsInstance(u_at, datetime)

    def test_date_format_for_updated_at(self):
        """
            Tests date format for datetime attribute
        """
        bm = BaseModel()
        u_at = bm.updated_at.__str__()
        u_at_pattern='\d{4}\-\d{2}\-\d{2}\ \d{2}\:\d{2}\:\d{2}\.\d{6}'
        self.assertRegex(u_at, u_at_pattern)

    def test_str_magic_function_with_empty_attributes(self):
        """
            Tests humain readable format
        """
        bm = BaseModel()
        s = bm.__str__()
        frmt = "[{}] ({}) {}".format(bm.__class__.__name__, bm.id, bm.__dict__)
        self.assertEqual(s, frmt)

    def test_str_magic_function_with_non_empty_attributes(self):
        """
            Tests humain readable format
        """
        bm = BaseModel()
        bm.name = "Betty"
        bm.year = 1917
        s = bm.__str__()
        frmt = "[{}] ({}) {}".format(bm.__class__.__name__, bm.id, bm.__dict__)
        self.assertEqual(s, frmt)

    def test_save_method_behavior_for_updating_attributres(self):
        """
            Tests Updated_at
        """
        bm = BaseModel()
        update_in_create = bm.updated_at
        bm.save()
        update_in_save = bm.updated_at
        self.assertNotEqual(update_in_create, update_in_save)

    def test_to_dict_behavior_for_dict_format_return(self):
        """
            Tests to_dict method
        """
        bm = BaseModel()
        bm.name = "Holberton"
        bm.number = 89
        bm_model = bm.to_dict()
        c_at = bm.created_at.isoformat()
        u_at = bm.updated_at.isoformat()
        bm_id = bm.id
        expected = {
            "name": "Holberton",
            "number": 89,
            "id": bm_id,
            "__class__": "BaseModel",
            "created_at": c_at,
            "updated_at": u_at
        }
        self.assertDictEqual(bm_model, expected)

    def test_to_dict_created_instance(self):
        """
            Tests attribute instance and type
        """
        bm = BaseModel()
        bm.name = "Betty"
        bm.number = 89
        bm_json = bm.to_dict()
        self.assertIsInstance(bm_json["number"], int)
        self.assertIsInstance(bm_json["name"], str)
        self.assertIsInstance(bm_json["__class__"], str)
        self.assertIsInstance(bm_json["updated_at"], str)
        self.assertIsInstance(bm_json["created_at"], str)
        self.assertIsInstance(bm_json["id"], str)
