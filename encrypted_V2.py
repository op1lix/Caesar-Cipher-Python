
title = "Caesar encryption program V2.0 by op1lix "
print(title.upper())

# НАСТРОЙКА ИНТЕРФЕЙСА
# Словарь с фразами: [English, Русский, Deutsch]
phrases = {
    "ask_lang": "Select language (1-EN, 2-RU, 3-DE): ",
    "ask_mode": ["1-Encrypt, 2-Decrypt :", "1-Зашифровать, 2-Расшифровать :", "1-Verschlüsseln, 2-Entschlüsseln :"],
    "ask_text": ["Enter text: ", "Введите текст: ", "Text eingeben: "],
    "ask_shift": ["Enter shift: ", "Введите сдвиг: ", "Verschiebung: "],
    "result": ["Result: ", "Результат: ", "Ergebnis: "]
}

#  ВЫБОР ЯЗЫКА
choice = int(input(phrases["ask_lang"]))
lang = choice - 1  # Превращаем 1, 2, 3 в индексы 0, 1, 2

#   ВВОД ДАННЫХ
# Используем индекс lang, чтобы программа говорила на выбранном языке
mode = int(input(phrases["ask_mode"][lang]))
text = input(phrases["ask_text"][lang]).lower()
shift = int(input(phrases["ask_shift"][lang]))
shift = shift + 10

if mode == 2:
    shift = -shift

#  АЛФАВИТ И ШИФРОВАНИЕ
EN_alphabet = "abcdefghijklmnopqrstuvwxyz"
RU_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
DE_extra = "äöüß"
result = ""

for char in text:
    if char in EN_alphabet:
        # Находим текущий номер буквы
        index = EN_alphabet.find(char)

        # % 26 не дает числу уйти выше 25
        new_index = (index + shift) % 26

        # Берем новую букву и добавляем в результат
        result += EN_alphabet[new_index]

    elif char in RU_alphabet:

        index = RU_alphabet.find(char)

        new_index = (index + shift) % 33

        result += RU_alphabet[new_index]

    elif char in DE_extra:
        index = DE_extra.find(char)
        new_index = (index + shift) % 4
        result += DE_extra[new_index]

    else:
        result += char

#   ВЫВОД
print(f"{phrases['result'][lang]} {result}")