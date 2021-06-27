import unittest

from gender_converter import convert_gender


class MyTestCase(unittest.TestCase):
    def test_something_female(self):
        expect="FEMALE"
        actual=convert_gender("F")
        self.assertEqual(actual, expect)
    def test_something_male(self):
        expect="MALE"
        actual=convert_gender("M")
        self.assertEqual(actual, expect)
    def test_something_unknown(self):
        expect="UNKNOWN"
        actual=convert_gender("HELLO")
        self.assertEqual(actual, expect)

if __name__ == '__main__':
    unittest.main()
