# Создайте функцию, которая удаляет из текста все символы кроме букв латинского алфавита и пробелов. Возвращается строка в нижнем регистре.
# from string import ascii_letters



def remover(text):
    latin = 'abcdefghijklmnopqrstuvwxyz '
    result_text = ''
    for letter in text.lower():
        if letter in latin:
            result_text += letter
    return result_text

text = "Hello world! How are you? 1111"
result_text = remover(text)

print(result_text)