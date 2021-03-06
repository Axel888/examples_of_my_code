print('Данная программа шифрует / дешифрует данные относительно "Шифра Цезаря" \n')

way = input('Укажите направление: шифрование или дешифрование. \n').lower()
while way != 'шифрование' and way != 'дешифрование':
    way = input('Пожалуйста, укажите корректное направление '
                '(шифрование / дешифрование) и проверьте правильность ввода. \n')
    continue

language = input('Укажите язык алфавита: русский или английский. \n')
while language.lower() != 'английский' and language.lower() != 'русский':
    language = input('Пожалуйста, укажите корректный язык '
                     '(русский / английский) и проверьте правильность ввода. \n')
    continue

step = input('Укажите в целом цифровом значении шаг сдвига (со сдвигом вправо). \n')
while True:
    if str(step).isdigit() == True:
        step = int(step)
        break
    else:
        step = input('Пожалуйста, укажите целое число шага кодировки. \n')
        continue

text = input('Введите текст: \n')

alphabet_ru_lower = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
alphabet_ru_upper = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alphabet_en_lower = 'abcdefghijklmnopqrstuvwxyz'
alphabet_en_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def encoding():
    answer = []

    if language.lower() == 'русский':
        letters = 32
        for i in text:
            if i == 'ё':
                i = i.replace('ё', 'е')
            if i == 'Ё':
                i = i.replace('Ё', 'Е')
            if i in alphabet_ru_lower:
                answer.append(alphabet_ru_lower[(alphabet_ru_lower.index(i) + step) % letters])
            elif i in alphabet_ru_upper:
                answer.append(alphabet_ru_upper[(alphabet_ru_upper.index(i) + step) % letters])
            else:
                answer.append(i)

    elif language.lower() == 'английский':
        letters = 26  # Количество букв в алфавите.
        for i in text:
            if i in alphabet_en_lower:
                answer.append(alphabet_en_lower[(alphabet_en_lower.index(i) + step) % letters])
            elif i in alphabet_en_upper:
                answer.append(alphabet_en_upper[(alphabet_en_upper.index(i) + step) % letters])
            else:
                answer.append(i)

    answer = ''.join(answer)
    return answer


def decoding():
    answer = []

    if language.lower() == 'русский':
        letters = 32
        for i in text:
            if i == 'ё':
                i = i.replace('ё', 'е')
            if i == 'Ё':
                i = i.replace('Ё', 'Е')
            if i in alphabet_ru_lower:
                answer.append(alphabet_ru_lower[(alphabet_ru_lower.index(i) - step) % letters])
            elif i in alphabet_ru_upper:
                answer.append(alphabet_ru_upper[(alphabet_ru_upper.index(i) - step) % letters])
            else:
                answer.append(i)

    elif language.lower() == 'английский':
        letters = 26
        for i in text:
            if i in alphabet_en_lower:
                answer.append(alphabet_en_lower[(alphabet_en_lower.index(i) - step) % letters])
            elif i in alphabet_en_upper:
                answer.append(alphabet_en_upper[(alphabet_en_upper.index(i) - step) % letters])
            else:
                answer.append(i)

    answer = ''.join(answer)
    return answer


if way == 'шифрование':
    print(f'\nРезультат: \n{encoding()}')
elif way == 'дешифрование':
    print(f'\nРезультат: \n{decoding()}')
