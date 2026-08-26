# Берем список улик из файла данных.
from data import CLUES

# Берем общие функции для красивого вывода улик и ожидания Enter.
from ui_helpers import print_field, print_option, print_title, wait_for_enter


# Создайте функцию, которая показывает улики.
def show_clues(game_state):
    # Нужно вывести заголовок "Улики".
    # Печатаем красивый заголовок раздела улик.
    print_title("Улики")
    # Нужно вывести разделитель через print_separator().
    # Разделитель уже печатает функция print_title().
    # Нужно пройти циклом по CLUES.
    for index, clue in enumerate(CLUES, start=1):
        # Для каждой улики нужно вывести номер, название и описание.
        # Печатаем название улики как пункт списка.
        print_option(index, clue["title"])
        # Печатаем описание улики отдельным полем с отступом.
        print_field("Описание", clue["description"])
        # Добавляем пустую строку между уликами, чтобы список читался легче.
        print()
        # Нужно добавлять название изученной улики в game_state["viewed_clues"].
        if clue["title"] not in game_state["viewed_clues"]:
            game_state["viewed_clues"].append(clue["title"])
    # Нужно вызвать wait_for_enter(), чтобы игрок успел прочитать улики.
    # Пустую строку перед подсказкой Enter добавляет wait_for_enter().
    wait_for_enter()
