import unittest
from leapyear import leap_year

class TestLeapYear(unittest.TestCase):
    #3 is not a leap year, should be False
    def test_correct(self):
        self.assertEqual(leap_year(3), False)
    #4 is a leap year, should be True
    def test_correct2(self):
        self.assertEqual(leap_year(4), True)
    #400 is a leap year, should be True
    def test_correct3(self):
        self.assertEqual(leap_year(400), True)
    #100 is not a leap year, should be false
    def test_correct4(self):
        self.assertEqual(leap_year(100), False)
    #0 is not a leap year, should be false
    def test_incorrect(self):
        self.assertEqual(leap_year(0), False)
    #Negative numbers should not be allowed
    def test_negative(self):
        self.assertEqual(leap_year(-4), None)
    #Strings should not be allowed
    def test_negative(self):
        self.assertEqual(leap_year("4 BC"), None)
if __name__ == "__main__":
    unittest.main()