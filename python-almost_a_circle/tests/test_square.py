import unittest
from models.square import Square  # replace 'your_module' with the name of your module

class TestSquare(unittest.TestCase):
    def setUp(self):
        self.sq1 = Square(3, 1, 2, 1)
        self.sq2 = Square(5)

    def test_init(self):
        self.assertEqual(self.sq1.id, 1)
        self.assertEqual(self.sq1.size, 3)
        self.assertEqual(self.sq1.x, 1)
        self.assertEqual(self.sq1.y, 2)
        self.assertEqual(self.sq2.id, 2)
        self.assertEqual(self.sq2.size, 5)
        self.assertEqual(self.sq2.x, 0)
        self.assertEqual(self.sq2.y, 0)

    def test_str(self):
        self.assertEqual(str(self.sq1), "[Square] (1) 1/2 - 3")
        self.assertEqual(str(self.sq2), "[Square] (2) 0/0 - 5")

    def test_update(self):
        self.sq1.update(10, 10, 10, 10)
        self.assertEqual(self.sq1.id, 10)
        self.assertEqual(self.sq1.size, 10)
        self.assertEqual(self.sq1.x, 10)
        self.assertEqual(self.sq1.y, 10)

    def test_to_dictionary(self):
        self.assertEqual(self.sq1.to_dictionary(), {'id': 10, 'size': 10, 'x': 10, 'y': 10})

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
