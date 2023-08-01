import unittest
import one


class OneTest(unittest.TestCase):
    def test_add(self):
        self.assertAlmostEqual(one.add(2, 2), 4)
        self.assertEqual(one.add(4, 4), 8)

    def test_subtract(self):
        self.assertEqual(one.subtract(2, 2), 0)
        self.assertEqual(one.subtract(2, 0), 2)

    def test_multiply(self):
        self.assertEqual(one.multiply(3, 3), 9)
        self.assertEqual(one.multiply(10, 0), 0)

    def test_division(self):
        self.assertEqual(one.division(25, 5), 5)
        self.assertRaises(ZeroDivisionError, one.division, 4, 0)


if __name__ == '__main__':
    unittest.main()

# run test  python -m unittest test_one.py
# run test  python -m unittest -v test_one.py
# run test search python -m unittest discover
# run test search python -m unittest discover -v
