# fixtures

import unittest
from person import Pesron


class PersonTest(unittest.TestCase):
    def setUp(self):
        self.p1 = Pesron("mohammd", "rahimaee")
        self.p2 = Pesron("reza", "rahimaee")

    def tearDown(self):
        print("down...")

    def test_fullname(self):
        self.assertEqual(self.p1.fullname(), 'mohammd rahimaee')
        self.assertEqual(self.p2.fullname(), 'reza rahimaee')

    def test_email(self):
        self.assertEqual(self.p1.email(), 'mohammdrahimaee@gmail.com')
        self.assertEqual(self.p2.email(), 'rezarahimaee@gmail.com')


if __name__ == '__main__':
    unittest.main()
