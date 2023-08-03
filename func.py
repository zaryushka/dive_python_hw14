# Напишите для задачи 1 тесты unittest. Проверьте
# следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери
# символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)

# тест вынесен в отдельный файл test_func.py

def remover(text):
    """
    возврат строки без изменений
    >>> remover('hello world how are you')
    'hello world how are you'

    возврат строки с преобразованием регистра без потери символов
    >>> remover('Hello World How Are You')
    'hello world how are you'

    возврат строки с удалением знаков пунктуации
    >>> remover('Hello, world!!! How are you???')
    'hello world how are you'

    возврат строки с удалением букв других алфавитов
    >>> remover('Привет, мир! 2023 на дворе. wow-wow-wow')
    '     wowwowwow'

    возврат строки с учётом всех вышеперечисленных пунктов
    >>> remover('Hello world(привет мир)! How are you? 1111')
    'hello world  how are you '  
    """

    latin = 'abcdefghijklmnopqrstuvwxyz '
    result_text = ''
    for letter in text.lower():
        if letter in latin:
            result_text += letter
    return result_text


