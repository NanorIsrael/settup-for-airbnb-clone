#!/usr/bin/python3
""" Module for testing user"""
import unittest
from models.user import User
from models import storage
from datetime import datetime
from time import sleep
import os

class test_User(unittest.TestCase):
    """ """
    user = User()
    user.first_name = "John"
    user.password = "password"
    user.email = "john@alx.com"
    user.last_name = "john@alx.com"

    def test_user(self):
        """ """
      
    def test_first_name(self):
        """ """
        self.assertEqual(type(test_User.user.first_name), str)

    def test_last_name(self):
        """ """
        self.assertEqual(type(test_User.user.last_name), str)

    def test_email(self):
        """ """
        self.assertEqual(type(test_User.user.email), str)

    def test_password(self):
        """ """
        self.assertEqual(type(test_User.user.password), str)

class TestAnotherUserInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the AnotherUser class."""

    def test_no_args_instantiates(self):
        self.assertEqual(User, type(User()))
    
    def test_new_instance_stored_in_objects(self):
        self.assertIn(User(), storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(User().id))
    
    def test_id_is_public_str(self):
        self.assertEqual(str, type(User().id))
  
    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_email_is_public_str(self):
        self.assertEqual(str, type(User.email))

    def test_password_is_public_str(self):
        self.assertEqual(str, type(User.password))

    def test_first_name_is_public_str(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name_is_public_str(self):
        self.assertEqual(str, type(User.last_name))

    def test_two_users_unique_ids(self):
        au1 = User()
        au2 = User()
        self.assertNotEqual(au1.id, au2.id)

    def test_two_users_different_created_at(self):
        au1 = User()
        sleep(0.05)
        au2 = User()
        self.assertLess(au1.created_at, au2.created_at)

    def test_two_users_different_updated_at(self):
        au1 = User()
        sleep(0.05)
        au2 = User()
        self.assertLess(au1.updated_at, au2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        au = User()
        au.id = "123456"
        au.created_at = au.updated_at = dt
        au_str = au.__str__()
        self.assertIn("[User] (123456)", au_str)
        self.assertIn("'id': '123456'", au_str)
        self.assertIn("'created_at': " + dt_repr, au_str)
        self.assertIn("'updated_at': " + dt_repr, au_str)
    
    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        au = User()
        au.id = "123456"
        au.created_at = au.updated_at = dt
        au_str = au.__str__()
        self.assertIn("[User] (123456)", au_str)
        self.assertIn("'id': '123456'", au_str)
        self.assertIn("'created_at': " + dt_repr, au_str)
        self.assertIn("'updated_at': " + dt_repr, au_str)
    
    def test_args_unused(self):
        au = User(None)
        self.assertNotIn(None, au.__dict__.values())
    
    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        au = User(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(au.id, "345")
        self.assertEqual(au.created_at, dt)
        self.assertEqual(au.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)

class TestAnotherUserSave(unittest.TestCase):
    """Unittests for testing save method of the AnotherUser class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        au = User()
        sleep(0.05)
        first_updated_at = au.updated_at
        au.save()
        self.assertLess(first_updated_at, au.updated_at)

    def test_two_saves(self):
        au = User()
        sleep(0.05)
        first_updated_at = au.updated_at
        au.save()
        second_updated_at = au.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        au.save()
        self.assertLess(second_updated_at, au.updated_at)

    def test_save_with_arg(self):
        au = User()
        with self.assertRaises(TypeError):
            au.save(None)

    def test_save_updates_file(self):
        au = User()
        au.save()
        auid = "User." + au.id
        with open("file.json", "r") as f:
            self.assertIn(auid, f.read())


class TestAnotherUserToDict(unittest.TestCase):
    """Unittests for testing to_dict method of the AnotherUser class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(User().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        au = User()
        self.assertIn("id", au.to_dict())
        self.assertIn("created_at", au.to_dict())
        self.assertIn("updated_at", au.to_dict())
        self.assertIn("__class__", au.to_dict())

    def test_to_dict_contains_added_attributes(self):
        au = User()
        au.middle_name = "Betty"
        au.my_number = 98
        self.assertEqual("Betty", au.middle_name)
        self.assertIn("my_number", au.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        au = User()
        au_dict = au.to_dict()
        self.assertEqual(str, type(au_dict["id"]))
        self.assertEqual(str, type(au_dict["created_at"]))
        self.assertEqual(str, type(au_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        au = User()
        au.id = "123456"
        au.created_at = au.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'User',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(au.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        au = User()
        self.assertNotEqual(au.to_dict(), au.__dict__)

    def test_to_dict_with_arg(self):
        au = User()
        with self.assertRaises(TypeError):
            au.to_dict(None)
