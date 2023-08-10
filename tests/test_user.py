#!/usr/bin/python3
""" Module for testing user"""
import unittest
from models.user import User


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