import unittest
from models.base_model import Base
import re
from datetime import datetime, timedelta
from unittest.mock import patch

class TestBaseClass(unittest.TestCase):
    """Defines test for the base class"""
    def test_instance(self):
        """Defines test for the base instance"""
        b1 = Base()
        self.assertIsInstance(b1, Base)
    def test_id(self):
        """Defines test for the base id attr"""
        b1 = Base()
        b2 = Base()
        pattern = re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$', re.IGNORECASE)
        self.assertTrue(hasattr(b1, "id"))
        self.assertIsInstance(b1.id, str)
        self.assertNotEqual(b1.id, b2.id)
        self.assertTrue(pattern.match(b1.id))
    def test_save(self):
        """Defines test for the base save method"""
        expected_time = datetime.now()
        with patch('models.base_model.datetime') as mock_datetime:
            mock_datetime.now.return_value = expected_time
            b1 = Base()
            b1.save()
            self.assertEqual(expected_time.isoformat(), b1.updated_at)
    def test_to_dict(self):
        """Defines test for the base to_dict method"""
        bm1 = Base()
        self.assertIsInstance(bm1.to_dict(), dict)