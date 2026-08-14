# Берем данные дела из файла данных.
from data import CASE_DATA, SUSPECTS
# Берем финальные тексты из файла данных.
from data import RESULT_TEXTS
# Берем учебную функцию анализа версии игрока.
from deepseek_client import analyze_player_version


# Создайте функцию, которая печатает линию-разделитель.
def print_separator():
    # Нужно вывести в консоль строку из 60 символов "-".
    print("-" * 60)


# Создайте функцию, которая ждет нажатия Enter.
def wait_for_enter():
    # Нужно вызвать input() с текстом вроде "Нажми Enter, чтобы продолжить...".
    input("Нажми Enter, чтобы продолжить...")


# Создайте функцию, которая помогает выбрать подозреваемого.
def choose_suspect():
    # Нужно импортировать SUSPECTS из data.py или использовать готовый список подозреваемых.
    print("Список подозреваемых:")
    # Нужно показать список подозреваемых с номерами.
    print_separator()
    for index, suspect in enumerate(SUSPECTS, start=1):
        print(f"{index}. {suspect['name']} ({suspect['role']})")
    # Нужно получить выбор игрока через input().
    print()
    choice = input("Выбери подозреваемого: ").strip()
    if not choice.isdigit():
        return None
    suspect_index = int(choice) - 1
    if 0 <= suspect_index < len(SUSPECTS):
    # Нужно вернуть выбранного подозреваемого или None.
        return SUSPECTS[suspect_index]
    return None


# Создайте функцию, которая проводит финальное обвинение.
def make_accusation():
    # Нужно выбрать подозреваемого через функцию choose_suspect().
    suspect = choose_suspect()
    # Нужно показать заголовок "Финальное обвинение".
    print("\nФинальное обвинение")
    # Нужно вывести разделитель через print_separator().
    print_separator()
    # Нужно дать игроку выбрать подозреваемого через choose_suspect().
    if suspect is None:
    # Если подозреваемый не выбран, нужно показать ошибку и вернуть False.
        print("Такого подозреваемого нет.")
        wait_for_enter()
        return False
    # Нужно попросить игрока объяснить свою версию через input().
    player_version = input("Объясни свою версию: ").strip()
    # Нужно сравнить suspect["name"] с CASE_DATA["criminal"].
    is_correct = suspect["name"].lower() == CASE_DATA["criminal"].lower()
    # Если ответ правильный, нужно вывести RESULT_TEXTS["correct"].
    if is_correct:
        print(RESULT_TEXTS["correct"])
    # Если ответ неправильный, нужно вывести RESULT_TEXTS["wrong"].
    else:
        print(RESULT_TEXTS["wrong"])
    # Нужно вывести версию игрока.
    print(f"\n{RESULT_TEXTS['player_version_label']}: {player_version}")
    # Нужно вывести CASE_DATA["solution"].
    print(f"\n{RESULT_TEXTS['solution_label']}: {CASE_DATA['solution']}")
    # Можно вызвать analyze_player_version(), чтобы показать учебный комментарий.
    print(analyze_player_version(player_version, suspect["name"], CASE_DATA))
    # Нужно вызвать wait_for_enter().
    print()
    wait_for_enter()
    # Нужно вернуть True, чтобы main.py понял, что игра закончилась.
    return True


# Проверяем, что файл запущен напрямую.
if __name__ == "__main__":
    # Печатаем название проверки для ученика.
    print("Проверка файла final.py")
    # Пытаемся запустить финальное обвинение отдельно.
    try:
        # Запускаем функцию финального обвинения.
        result = make_accusation()
        # Печатаем результат функции.
        print(f"Функция вернула: {result}")
    # Ловим ошибку, если функция еще не реализована.
    except NotImplementedError as error:
        # Печатаем понятное сообщение для ученика.
        print(f"Нужно доделать задание: {error}")
