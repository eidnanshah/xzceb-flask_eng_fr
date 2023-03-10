import unittest
from machinetranslation.translator import english_to_french, french_to_english


class TestTranslation(unittest.TestCase):
    """Test cases for machine translation functions."""

    def test_english_to_french(self):
        """Test english_to_french function."""
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french(''), '')
        self.assertIsNone(english_to_french(None))
        self.assertNotEqual(english_to_french('Hello'), 'Hello')

    def test_french_to_english(self):
        """Test french_to_english function."""
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english(''), '')
        self.assertIsNone(french_to_english(None))
        self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour')


if __name__ == '__main__':
    unittest.main()
