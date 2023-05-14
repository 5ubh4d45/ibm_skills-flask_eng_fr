import unittest
from translator import englishToFrench, frenchToEnglish

# test cases for englishToFrench function and frenchToEnglish function
class TestEnglishToFrench(unittest.TestCase):
    # test case for englishToFrench function
    def test_englishToFrench(self):
        # for Hello to Bonjour
        self.assertEqual(englishToFrench('Hello'), 'Bonjour',
                         'Should be Bonjour')
        self.assertNotEqual(englishToFrench('Hello'), 'Hello',
                            'Should not be Hello')

        # for empty string
        self.assertEqual(englishToFrench(''), '', 
                         'Should be empty string')
        self.assertEqual(englishToFrench(' '), ' ',
                         'Should be empty string')

        # for null value
        self.assertEqual(englishToFrench(None), None,
                         'Should be null value')

    # test case for frenchToEnglish function
    def test_frenchToEnglish(self):
        # for Bonjour to Hello
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello',
                         'Should be Hello')
        self.assertNotEqual(frenchToEnglish('Bonjour'), 'Bonjour',
                            'Should not be Bonjour')

        # for empty string
        self.assertEqual(frenchToEnglish(''), '',
                         'Should be empty string')
        self.assertEqual(frenchToEnglish(' '), ' ',
                         'Should be empty string')

        # for null value
        self.assertEqual(frenchToEnglish(None), None,
                         'Should be null value')
        
unittest.main()