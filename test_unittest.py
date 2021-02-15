# raise TypeError - выкидывает ошибку TypeError

# terminal: pip freeze>requirements.txt - сщздает файл с версиями всех пакетов используемых в этом окружении
# pip install -r requirements.txt - установка всех пакетов из файла

import unittest


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")

    def test_abs2(self):
        self.assertEqual(abs(-42), -42, "Should be absolute value of a number")


if __name__ == "__main__":
    unittest.main()