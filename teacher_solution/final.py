# Берем учебную функцию анализа версии игрока.
from ai_client import analyze_player_version

# Берем данные дела, подозреваемых и финальные тексты из файла данных.
from data import CASE_DATA, RESULT_TEXTS, SUSPECTS

# Берем общие функции для ввода, красивого вывода финала и ожидания Enter.
from ui_helpers import (
    ask_number,
    ask_text,
    print_field,
    print_option,
    print_title,
    wait_for_enter,
)


# Создайте функцию, которая помогает выбрать подозреваемого.
def choose_suspect():
    # Нужно импортировать SUSPECTS из data.py или использовать готовый список подозреваемых.
    # Печатаем красивый заголовок списка подозреваемых.
    print_title("Список подозреваемых")
    # Нужно показать список подозреваемых с номерами.
    # Разделитель уже печатает функция print_title().
    for index, suspect in enumerate(SUSPECTS, start=1):
        # Печатаем подозреваемого как пункт выбора.
        print_option(index, f"{suspect['name']} ({suspect['role']})")
    # Нужно получить выбор игрока через input().
    print()
    suspect_index = ask_number(len(SUSPECTS), "Выбери подозреваемого: ")
    # Нужно вернуть выбранного подозреваемого или None.
    return SUSPECTS[suspect_index]


# Создайте функцию, которая проводит финальное обвинение.
def make_accusation():
    # Нужно выбрать подозреваемого через функцию choose_suspect().
    suspect = choose_suspect()
    # Нужно показать заголовок "Финальное обвинение".
    # Печатаем красивый заголовок финального обвинения.
    print_title("Финальное обвинение")
    # Нужно вывести разделитель через print_separator().
    # Разделитель уже печатает функция print_title().
    # Нужно попросить игрока объяснить свою версию через input().
    player_version = ask_text("Объясни свою версию: ")
    # Нужно сравнить suspect["name"] с CASE_DATA["criminal"].
    is_correct = suspect["name"].lower() == CASE_DATA["criminal"].lower()
    # Если ответ правильный, нужно вывести RESULT_TEXTS["correct"].
    if is_correct:
        # Печатаем красивый заголовок результата.
        print_title("Результат")
        print(RESULT_TEXTS["correct"])
    # Если ответ неправильный, нужно вывести RESULT_TEXTS["wrong"].
    else:
        # Печатаем красивый заголовок результата.
        print_title("Результат")
        print(RESULT_TEXTS["wrong"])
    # Нужно вывести версию игрока.
    print()
    # Печатаем версию игрока отдельным полем.
    print_field(RESULT_TEXTS["player_version_label"], player_version)
    # Нужно вывести CASE_DATA["solution"].
    print()
    # Печатаем правильное решение отдельным полем.
    print_field(RESULT_TEXTS["solution_label"], CASE_DATA["solution"])
    # Можно вызвать analyze_player_version(), чтобы показать учебный комментарий.
    print(analyze_player_version(player_version, suspect["name"], CASE_DATA))
    # Нужно вызвать wait_for_enter().
    print()
    wait_for_enter()
    # Нужно вернуть True, чтобы main.py понял, что игра закончилась.
    return True
