#!/usr/bin/python3

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseDict(unittest.TestCase):
    """
        Tests base model dictionary
    """
    def test_instance_creation_with_kwargs_single_argument(self):
        """
            Test instance creation with kwargs
        """
        kwargs = {"name": "Betty"}
        bm = BaseModel(**kwargs)
        self.assertEqual(bm.name, "Betty")

    def test_instance_creation_with_kwargs_multi_args(self):
        """
            Test instance
        """
        kwargs = {"name": "Betty", "number": 89}
        bm = BaseModel(**kwargs)
        self.assertEqual(bm.name, "Betty")
        self.assertEqual(bm.number, 89)

    def test_instance_creation_with_id(self):
        """
            Test predefined id
        """
        b_id = 'c1586632-9ab1-4894-a5d9-fe55c1571ef1'
        kwargs = {"id": b_id}
        bm = BaseModel(**kwargs)
        self.assertEqual(bm.id, b_id)

    def test_instance_creation_with_created_at_as_datetime(self):
        """
            Tests created at
        """
        c_at = '2017-09-28T21:03:54.052302'
        kwargs = {"created_at": c_at}
        bm = BaseModel(**kwargs)
        self.assertIsInstance(bm.created_at, datetime)

    def test_instance_creation_with_updated_at_as_datetime(self):
        """
            Tests updated at
        """
        u_at = '2017-09-28T21:03:54.052302'
        kwargs = {"updated_at": u_at}
        bm = BaseModel(**kwargs)
        self.assertIsInstance(bm.updated_at, datetime)

    def test_instance_creation_with_created_at_attr(self):
        """
            Tests created at
        """
        c_at = '2017-09-28T21:03:54.052302'
        kwargs = {"created_at": c_at}
        bm = BaseModel(**kwargs)
        c_expected = datetime(2017, 9, 28, 21, 3, 54, 52302)
        self.assertEqual(bm.created_at, c_expected)

    def test_instance_creation_with_created_at_attr(self):
        """
            Tests updated at
        """
        u_at = '2017-09-28T21:03:54.052302'
        kwargs = {"updated_at": u_at}
        bm = BaseModel(**kwargs)
        u_expected = datetime(2017, 9, 28, 21, 3, 54, 52302)
        self.assertEqual(bm.updated_at, u_expected)

    def test_should_not_add__class__to_the_attributes(self):
        """
            Tests should not add __class__ to the attribute
        """
        kwargs = {"__class__": "FakeBaseModel"}
        bm = BaseModel(**kwargs)
        self.assertNotEqual(bm.__class__, "FakeBaseModel")

    def test_should_add__class__to_the_attributes(self):
        """
            Tests should not add __class__ to the attribute
        """
        kwargs = {"__class__": "FakeBaseModel"}
        bm = BaseModel(**kwargs)
        self.assertEqual(str(bm.__class__),
                         "<class 'models.base_model.BaseModel'>")
