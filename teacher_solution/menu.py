# Берем название игры, пункты главного меню и правила из файла данных.
from data import GAME_TITLE, MAIN_MENU_ITEMS, RULES_TEXT

# Берем общие функции для ввода, красивого вывода пунктов, заголовков и ожидания Enter.
from ui_helpers import ask_option, print_option, print_title, wait_for_enter


# Создайте функцию, которая показывает правила игры.
def show_rules():
    # Нужно вывести заголовок "Правила игры".
    # Печатаем красивый заголовок раздела правил.
    print_title("Правила игры")
    # Нужно вывести разделитель через print_separator().
    # Разделитель уже печатает функция print_title().
    # Нужно пройти циклом по RULES_TEXT и напечатать каждое правило.
    for rule_number, rule in enumerate(RULES_TEXT, start=1):
        # Печатаем правило как аккуратный пункт списка.
        print_option(rule_number, rule)
    # Нужно вызвать wait_for_enter(), чтобы игрок успел прочитать правила.
    # Пустую строку перед подсказкой Enter добавляет wait_for_enter().
    wait_for_enter()


# Создайте функцию, которая показывает главное меню.
def show_main_menu():
    # Нужно вывести GAME_TITLE.
    # Печатаем красивый заголовок с названием игры.
    print_title(GAME_TITLE)
    # Нужно вывести разделитель через print_separator().
    # Разделитель уже печатает функция print_title().
    # Нужно пройти циклом по MAIN_MENU_ITEMS и вывести номер с названием пункта.
    for menu_key, menu_text in MAIN_MENU_ITEMS.items():
        # Печатаем пункт главного меню с единым отступом.
        print_option(menu_key, menu_text)
    # Нужно получить выбор игрока через input().
    print()
    choice = ask_option(
        MAIN_MENU_ITEMS,
        "Выбери пункт: ",
        "Такого пункта нет. Попробуй еще раз.",
    )
    # Нужно вернуть выбор игрока через return.
    return choice
