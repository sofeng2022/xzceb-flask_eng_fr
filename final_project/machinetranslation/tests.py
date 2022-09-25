import unittest

from translator import french_to_english, english_to_french

class TestFrench_To_English(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english(0), '0')
        self.assertNotEqual(french_to_english(0), 0)
        self.assertEqual(french_to_english('Hello'), 'Hello')
        self.assertNotEqual(french_to_english('Hello'), '0')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Bonjour'), '0')

class TestEnglish_To_French(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french(0), 'Bonjour, comment es-tu?')
        self.assertNotEqual(english_to_french(0), 0)
        self.assertEqual(english_to_french('Bonjour'), 'Bonjour, comment es-tu?')
        self.assertNotEqual(english_to_french('Bonjour'), 'Hello')
        self.assertEqual(english_to_french('Hello'), 'Bonjour, comment es-tu?')
        self.assertNotEqual(english_to_french('Hello'), 'Hello')

unittest.main()  
