import unittest
import example2
import random
from datetime import datetime


class Example2Test(unittest.TestCase):
    def test1(self):
        for j in range(0, 9999999999999999):
            for i in range(1900, 1999):
                print("\n\n")
                month = random.randint(1, 12)
                day = random.randint(1,28)
                dt = datetime(i, month, day)
                self.assertEqual(example2.whatDay(i, month, day), dt.weekday())