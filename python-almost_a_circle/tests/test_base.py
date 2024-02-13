import unittest
import os
import json
from models.base import Base  # replace 'your_module' with the name of your module

class TestBase(unittest.TestCase):
    def setUp(self):
        self.base1 = Base(1)
        self.base2 = Base()

    def test_init(self):
        self.assertEqual(self.base1.id, 1)
        self.assertEqual(self.base2.id, 2)

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{'id': 1}]), '[{"id": 1}]')

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string('[{"id": 1}]'), [{'id': 1}])

    def test_save_to_file(self):
        Base.save_to_file([self.base1, self.base2])
        with open("Base.json", "r") as file:
            self.assertEqual(json.load(file), [{'id': 1}, {'id': 2}])

    def test_load_from_file(self):
        Base.save_to_file([self.base1, self.base2])
        bases = Base.load_from_file()
        self.assertIsInstance(bases, list)
        self.assertEqual(len(bases), 2)
        self.assertEqual(bases[0].id, 1)
        self.assertEqual(bases[1].id, 2)

    def tearDown(self):
        try:
            os.remove("Base.json")
        except:
            pass

if __name__ == "__main__":
    unittest.main()
