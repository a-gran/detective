# Берем данные дела из файла данных.
from data import CASE_DATA

# Берем общие функции для красивого заголовка и ожидания Enter.
from ui_helpers import print_title, wait_for_enter


# Создайте функцию, которая показывает описание дела.
def show_case_description():
    # Нужно вывести название дела из CASE_DATA["title"].
    # Печатаем название дела как красивый заголовок.
    print_title(CASE_DATA["title"])
    # Нужно вывести разделитель через print_separator().
    # Разделитель уже печатает функция print_title().
    # Нужно вывести описание дела из CASE_DATA["description"].
    print(CASE_DATA["description"])
    # Нужно вызвать wait_for_enter(), чтобы игрок успел прочитать дело.
    # Пустую строку перед подсказкой Enter добавляет wait_for_enter().
    wait_for_enter()
