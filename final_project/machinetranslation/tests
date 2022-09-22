import unittest

from translator import english_to_french, french_to_english

class TestenglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french(0), 0)
        self.assertNotEqual(english_to_french(0), 0)
        self.assertEqual(english_to_french('Bonjour'), 0)
        self.assertEqual(english_to_french('Hello'), 0)
        self.assertNotEqual(english_to_french('Bonjour'), 0)
        self.assertNotEqual(english_to_french('Hello'), 0)

class TestfrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english(0), 0)
        self.assertNotEqual(french_to_english(0), 0)
        self.assertEqual(french_to_english('Hello'), 0)
        self.assertEqual(french_to_english('Bonjour'), 0)
        self.assertNotEqual(french_to_english('Hello'), 0)
        self.assertNotEqual(french_to_english('Bonjour'), 0)

unittest.main()
