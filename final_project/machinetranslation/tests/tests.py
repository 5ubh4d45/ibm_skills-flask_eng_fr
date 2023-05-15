import unittest
from ..translator import english_to_french, french_to_english


# test cases for englishToFrench function and frenchToEnglish function
class TestEnglishToFrench(unittest.TestCase):
    # test case for englishToFrench function
    def test_englishToFrench(self):
        # for Hello to Bonjour
        self.assertEqual(english_to_french('Hello'), 'Bonjour',
                         'Should be Bonjour')
        self.assertNotEqual(english_to_french('Hello'), 'Hello',
                            'Should not be Hello')

        # for empty string
        self.assertEqual(english_to_french(''), '',
                         'Should be empty string')
        self.assertEqual(english_to_french(' '), '',
                         'Should be empty string')

        # for null value
        self.assertEqual(english_to_french(None), "",
                         'Should be empty string')

    # test case for frenchToEnglish function
    def test_frenchToEnglish(self):
        # for Bonjour to Hello
        self.assertEqual(french_to_english('Bonjour'), 'Hello',
                         'Should be Hello')
        self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour',
                            'Should not be Bonjour')

        # for empty string
        self.assertEqual(french_to_english(''), '',
                         'Should be empty string')
        self.assertEqual(french_to_english(' '), '',
                         'Should be empty string')

        # for null value
        self.assertEqual(french_to_english(None), "",
                         'Should be empty string')


if __name__ == '__main__':
    unittest.main()
