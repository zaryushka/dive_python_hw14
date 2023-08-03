# Напишите для задачи 1 тесты pytest. Проверьте следующие
# варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери
# символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)

import pytest

def test_not_change(*args, **kwargs):
    assert remover('Hello, world(мир)444! How are you') == 'hello world how are you'

def test_is_register(*args, **kwargs):
    # assert not remover('Hello World How Are You')
    assert remover('hello world how are you')

def test_simbols(*args, **kwargs):
    assert not remover('125365')

def test_atrr_error(*args, **kwargs):
    with pytest.raises(AttributeError):
        remover(111)



def remover(text):
    latin = 'abcdefghijklmnopqrstuvwxyz '
    result_text = ''
    for letter in text.lower():
        if letter in latin:
            result_text += letter
    return result_text

if __name__ == '__main__':
    pytest.main(['-v'])