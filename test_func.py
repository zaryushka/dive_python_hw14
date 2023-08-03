import unittest
from func import remover

class TestString(unittest.TestCase):

    def test_not_change(self):
        self.assertEqual(remover('hello world how are you'), 'hello world how are you')

    def test_register(self):
        self.assertEqual(remover('Hello World How Are You'), 'hello world how are you')

    def test_punctuation(self):
        self.assertEqual(remover('Hello, world!!! How are you???'), 'hello world how are you')

    def test_only_latin(self):
        self.assertEqual(remover('Привет, мир! 2023 на дворе. wow-wow-wow'), '     wowwowwow')

    def test_all(self):
        self.assertEqual(remover('Hello world(привет мир)! How are you? 1111'), 'hello world  how are you ')

if __name__ == '__main__':
    unittest.main(verbosity=2)