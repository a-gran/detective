# Берем настройки сложности из файла данных.
from data import DIFFICULTY_SETTINGS

# Берем общие функции для ввода и красивого вывода сложности.
from ui_helpers import ask_option, print_field, print_option, print_title


# Создайте функцию, которая просит игрока выбрать сложность.
def choose_difficulty():
    # Нужно показать заголовок "Выбор сложности".
    while True:
        # Печатаем красивый заголовок выбора сложности.
        print_title("Выбор сложности")
        # Нужно вывести разделитель через print_separator().
        # Разделитель уже печатает функция print_title().
        # Нужно пройти циклом по DIFFICULTY_SETTINGS и показать все варианты.
        for difficulty_key, difficulty_data in DIFFICULTY_SETTINGS.items():
            # Печатаем название сложности как пункт списка.
            print_option(difficulty_key, difficulty_data["name"])
            # Печатаем описание сложности отдельной строкой с отступом.
            print_field("Описание", difficulty_data["description"])
            # Добавляем пустую строку между сложностями, чтобы варианты не слипались.
            print()
        # Нужно получить выбор игрока через input().
        print()
        choice = ask_option(
            DIFFICULTY_SETTINGS,
            "Выбери сложность: ",
            "Такого варианта нет. Попробуй еще раз.",
        )
        # Нужно проверить, есть ли такой ключ в DIFFICULTY_SETTINGS.
        # Если выбор правильный, нужно вернуть словарь выбранной сложности.
        return DIFFICULTY_SETTINGS[choice]
