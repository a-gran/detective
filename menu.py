# Берем название игры из файла данных.
from data import GAME_TITLE
# Берем пункты главного меню из файла данных.
from data import MAIN_MENU_ITEMS
# Берем правила игры из файла данных.
from data import RULES_TEXT


# Создайте функцию, которая печатает линию-разделитель.
def print_separator():
    # Нужно вывести в консоль строку из 60 символов "-".
    print("-" * 60)


# Создайте функцию, которая ждет нажатия Enter.
def wait_for_enter():
    # Нужно вызвать input() с текстом вроде "Нажми Enter, чтобы продолжить...".
    input("Нажми Enter, чтобы продолжить...")


# Создайте функцию, которая показывает правила игры.
def show_rules():
    # Нужно вывести заголовок "Правила игры".
    print("\n ====================== Правила игры ====================== ")
    # Нужно вывести разделитель через print_separator().
    print_separator()
    # Нужно пройти циклом по RULES_TEXT и напечатать каждое правило.
    for rule_number, rule in enumerate(RULES_TEXT, start=1):
        print(f"{rule_number}. {rule}")
    # Нужно вызвать wait_for_enter(), чтобы игрок успел прочитать правила.
    print()
    wait_for_enter()


# Создайте функцию, которая показывает главное меню.
def show_main_menu():
    # Нужно вывести GAME_TITLE.
    print(f"\n{GAME_TITLE}")
    # Нужно вывести разделитель через print_separator().
    print_separator()
    # Нужно пройти циклом по MAIN_MENU_ITEMS и вывести номер с названием пункта.
    for menu_key, menu_text in MAIN_MENU_ITEMS.items():
        print(f"{menu_key}. {menu_text}")
    # Нужно получить выбор игрока через input().
    print()
    choice = input("Выбери пункт: ").strip()
    # Нужно вернуть выбор игрока через return.
    return choice


# Проверяем, что файл запущен напрямую.
if __name__ == "__main__":
    # Печатаем название проверки для ученика.
    print("Проверка файла menu.py")
    # Пытаемся проверить функции главного меню.
    try:
        # Показываем правила игры.
        show_rules()
        # Показываем главное меню и сохраняем выбор.
        choice = show_main_menu()
        # Печатаем выбор игрока.
        print(f"Выбран пункт: {choice}")
    # Ловим ошибку, если функция еще не реализована.
    except NotImplementedError as error:
        # Печатаем понятное сообщение для ученика.
        print(f"Нужно доделать задание: {error}")
