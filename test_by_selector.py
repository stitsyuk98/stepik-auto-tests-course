import unittest
from by_selector import check


class TestAbs(unittest.TestCase):
    def test_check1(self):
        self.assertEqual(check('http://suninjuly.github.io/registration1.html'),
                         "Congratulations! You have successfully registered!",
                         "should be good")

    def test_check2(self):
        self.assertEqual(check('http://suninjuly.github.io/registration2.html'),
                         "Congratulations! You have successfully registered!",
                         "should be good")


if __name__ == "__main__":
    unittest.main()