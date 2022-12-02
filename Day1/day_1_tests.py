import unittest
from day_1 import *
example = '1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000'
class test_max_calorie_elf(unittest.TestCase):

    def test_one_elf(self):
        self.assertEqual(max_calorie_elf('100\n200'), 1)
    
    def test_two_elf(self):
        self.assertEqual(max_calorie_elf('100\n200\n\n400'), 2)

    def test_equal_elf(self):
        self.assertEqual(max_calorie_elf('200\n200\n\n400'), 1)

    def test_no_items(self):
        self.assertEqual(max_calorie_elf('0\n0\n\n0'), 0)

    def test_example_given(self):
        self.assertEqual(max_calorie_elf(example), 4)

class test_calorie_count(unittest.TestCase):

    def test_multiple_items(self):
        self.assertEqual(calorie_count('100\n200'),300)
        
    def test_single_item(self):
        self.assertEqual(calorie_count('100'),100)

if __name__ == '__main__':
    unittest.main()