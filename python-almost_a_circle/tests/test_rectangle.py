import unittest
from models.rectangle import Rectangle  # replace 'your_module' with the name of your module

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rect1 = Rectangle(3, 4, 1, 2, 1)
        self.rect2 = Rectangle(5, 6)

    def test_init(self):
        self.assertEqual(self.rect1.id, 1)
        self.assertEqual(self.rect1.width, 3)
        self.assertEqual(self.rect1.height, 4)
        self.assertEqual(self.rect1.x, 1)
        self.assertEqual(self.rect1.y, 2)
        self.assertEqual(self.rect2.id, 2)
        self.assertEqual(self.rect2.width, 5)
        self.assertEqual(self.rect2.height, 6)
        self.assertEqual(self.rect2.x, 0)
        self.assertEqual(self.rect2.y, 0)

    def test_area(self):
        self.assertEqual(self.rect1.area(), 12)
        self.assertEqual(self.rect2.area(), 30)

    def test_str(self):
        self.assertEqual(str(self.rect1), "[Rectangle] (1) 1/2 - 3/4")
        self.assertEqual(str(self.rect2), "[Rectangle] (2) 0/0 - 5/6")

    def test_update(self):
        self.rect1.update(10, 10, 10, 10, 10)
        self.assertEqual(self.rect1.id, 10)
        self.assertEqual(self.rect1.width, 10)
        self.assertEqual(self.rect1.height, 10)
        self.assertEqual(self.rect1.x, 10)
        self.assertEqual(self.rect1.y, 10)

    def test_to_dictionary(self):
        self.assertEqual(self.rect1.to_dictionary(), {'id': 10, 'width': 10, 'height': 10, 'x': 10, 'y': 10})

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
