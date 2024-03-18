import unittest
from plus import plus


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def test1(self):
        self.assertEquals(plus(1, 2), 3)

    def test2(self):
        self.assertEquals(plus(2, 3), 5)

    def test3(self):
        self.assertEquals(plus(3, 17), 20)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
