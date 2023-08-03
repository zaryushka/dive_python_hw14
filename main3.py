# Напишите для задачи 1 тесты unittest. Проверьте
# следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери
# символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)

import unittest

class TestString(unittest.TestCase):

    def test_not_change(self):
        self.assertEqual(remover('hello world how are you'), 'hello world how are you')

    def test_register(self):
        self.assertEqual(remover('Hello World How Are You'), 'hello world how are you')
    
    def test_punctuation(self):
        self.assertEqual(remover('hello, world!!! how are you???'), 'hello world how are you')    

    def test_only_latin(self):
        self.assertEqual(remover('Привет, мир! 2023 на дворе. wow-wow-wow'), '     wowwowwow')

    def test_all(self):
        self.assertEqual(remover('Hello world(привет мир)! How are you? 1111'), 'hello world  how are you ')     



def remover(text):

    latin = 'abcdefghijklmnopqrstuvwxyz '
    result_text = ''
    for letter in text.lower():
        if letter in latin:
            result_text += letter
    return result_text


unittest.main(verbosity=2)
