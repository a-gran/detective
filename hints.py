# Берем список подсказок из файла данных.
from data import HINTS


# Создайте функцию, которая ждет нажатия Enter.
def wait_for_enter():
    # Нужно вызвать input() с текстом вроде "Нажми Enter, чтобы продолжить...".
    input("Нажми Enter, чтобы продолжить...")


# Создайте функцию, которая показывает подсказку.
def show_hint(game_state):
    # Нужно проверить, остались ли подсказки в game_state["hints_left"].
    if game_state["hints_left"] <= 0:
    # Если подсказок нет, нужно показать сообщение и завершить функцию.
        print("Подсказок больше нет!")
        wait_for_enter()
        return
    # Нужно вычислить номер следующей подсказки.
    hint_index = len(HINTS) - game_state["hints_left"]
    if hint_index >= len(HINTS):
        hint_index = len(HINTS) - 1
    current_hint = HINTS[hint_index]
    # Нужно уменьшить game_state["hints_left"] на 1.
    game_state["hints_left"] -= 1
    # Нужно вывести подсказку.
    print(f"\nПодсказка: {current_hint}")
    # Нужно вывести количество оставшихся подсказок.
    print(f"Осталось подсказок: {game_state['hints_left']}")
    # Нужно вызвать wait_for_enter().
    print()
    wait_for_enter()


# Проверяем, что файл запущен напрямую.
if __name__ == "__main__":
    # Печатаем название проверки для ученика.
    print("Проверка файла hints.py")
    # Создаем тестовое состояние игры.
    test_state = {"hints_left": 2}
    # Пытаемся показать подсказку отдельно.
    try:
        # Запускаем функцию показа подсказки.
        show_hint(test_state)
        # Печатаем состояние после подсказки.
        print(test_state)
    # Ловим ошибку, если функция еще не реализована.
    except NotImplementedError as error:
        # Печатаем понятное сообщение для ученика.
        print(f"Нужно доделать задание: {error}")
