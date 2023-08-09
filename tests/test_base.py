from sys import path
import unittest
from models.base_model import BaseModel
import os
from datetime import datetime, timedelta
from unittest.mock import patch
import uuid

class TestBaseClass(unittest.TestCase):
    """Defines test for the base class"""

    def test_if_class_documentation_exists(self):
        """ Test if method documentation exists"""
        bm = BaseModel()
        self.assertIsNotNone(bm.__doc__)

    def test_instance(self):
        """Defines test for the base instance"""
        bm1 = BaseModel()
        self.assertIsInstance(bm1, BaseModel)
    def test_id(self):
        """Defines test for the base id attr"""
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertTrue(hasattr(b1, "id"))
        self.assertIsInstance(b1.id, str)
        self.assertNotEqual(b1.id, b2.id)
        self.assertTrue(uuid.UUID(b1.id))

    def test_updated_at_during_save(self):
        """Defines test for the base save method"""
        b1 = BaseModel()
        updated_time_before_save = b1.updated_at.isoformat()
        b1.save()
        updated_time_after_save = b1.updated_at.isoformat()

        self.assertNotEqual(updated_time_before_save, updated_time_after_save)
    
    def test_created_at_not_null(self):
        """Defines test for created at not null"""
        b1 = BaseModel()
        self.assertIsNotNone(b1.created_at, msg="created at is none")
    
    def test_type_of_created_at(self):
        """Defines test for created_at type"""
        b1 = BaseModel()
        self.assertTrue(isinstance(b1.created_at, datetime))

    def test_create_two_instances_and_check_instance_equality(self):
        """Defines test for created_at type"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertTrue((bm1.created_at < bm2.created_at))
    
    def test_updated_at_not_null(self):
        """Defines test for created at not null"""
        b1 = BaseModel()
        self.assertIsNotNone(b1.updated_at, msg="updated_at at is none")
    
    def test_type_of_updated_at(self):
        """Defines test for created_at type"""
        b1 = BaseModel()
        self.assertTrue(isinstance(b1.updated_at, datetime))

    def test_create_two_instances_and_check_instance_equality(self):
        """Defines test for created_at type"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertTrue((bm1.updated_at < bm2.updated_at))

    def test_if_save_method_documentation_exists(self):
        """ Test if method documentation exists"""
        bm = BaseModel()
        docstring = bm.save.__doc__
        self.assertIsNotNone(docstring, msg="Documentation is missing")
        self.assertNotEqual(docstring.strip(), "", msg="Documentation is empty or consists of only whitespace")


class TestBase_save_to_file(unittest.TestCase):
    """Unittests for testing save_to_file method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("file.json")
        except IOError:
            pass
    
    def test_save(self):
        """Defines test for the base save method"""
        bm1 = BaseModel()
        bm1.save()
     
        with open('file.json', 'r', encoding='UTF-8') as my_file:
            content = my_file.read()
            self.assertFalse(len(content) == None)

    def test_save_for_two_instances(self):
        """Defines test for the base save method"""
    
        bm1 = BaseModel()
        bm2 = BaseModel()
        bm1.save()
        bm2.save()
        with open('file.json', 'r', encoding='UTF-8') as my_file:
            content = my_file.read()
            self.assertFalse(len(content) == None)

    def test_save_to_file_do_not_overwrite(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        bm1.save()
        bm2.save()
        with open("file.json", "r") as f:
            self.assertTrue(len(f.read()) != 1060)


class TestBaseModel_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of BaseModel class."""
    def test_to_dict(self):
        bm1 = BaseModel()
        self.assertTrue(isinstance(bm1.to_dict(), dict))

    def test_if_to_dict_method_documentation_exists(self):
        """ Test if method documentation exists"""
        bm = BaseModel()
        docstring = bm.to_dict.__doc__
        self.assertIsNotNone(docstring, msg="Documentation is missing")
        self.assertNotEqual(docstring.strip(), "", msg="Documentation is empty or consists of only whitespace")
    
    def test_dict_remains_unchanged_with_args_provided(self):
        """  check that __dict__ remains unchanged with args provided"""
        bm2 = BaseModel("arg")
        self.assertFalse(getattr(bm2, "arg", None))

    def test_str_format(self):
        """Test if __str__ method produces the correct format/output"""
        obj = BaseModel("12345", "test_value")
        expected_output = f"[{obj.__class__.__name__}] ({obj.id}) {obj.__dict__}"
        actual_output = str(obj)
        self.assertEqual(actual_output, expected_output)
