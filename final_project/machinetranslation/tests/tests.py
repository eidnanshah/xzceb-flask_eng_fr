"""Unit tests for the machinetranslation package."""
import unittest
from machinetranslation import (english_to_french, french_to_english)

class TestTranslation(unittest.TestCase):
    """Test cases for machine translation functions."""

    def test_english_to_french(self):
        """Test english_to_french function."""
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french(''), '')
        self.assertIsNone(english_to_french(None))
        self.assertRaises(Exception, english_to_french, 123)

    def test_french_to_english(self):
        """Test french_to_english function."""
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english(''), '')
        self.assertIsNone(french_to_english(None))
        self.assertRaises(Exception, french_to_english, 123)

if __name__ == '__main__':
    unittest.main()
