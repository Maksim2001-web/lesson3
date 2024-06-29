my_string = input("Введите произвольный текст: ")
print("Количество символов:", len(my_string))

# Работа с методами строк
print("Строка в верхнем регистре:", my_string.upper())
print("Строка в нижнем регистре:", my_string.lower())
print("Строка без пробелов:", my_string.replace(" ", ""))
print("Первый символ:", my_string[0])
print("Последний символ:", my_string[-1])