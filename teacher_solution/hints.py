# Берем функцию AI-переформулировки подсказки.
from ai_client import rewrite_hint_with_ai
# Берем список подсказок из файла данных.
from data import CASE_DATA, HINTS

# Берем общие функции для красивого вывода подсказки и ожидания Enter.
from ui_helpers import print_field, print_title, wait_for_enter


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
    # Просим AI переформулировать уже выбранную кодом подсказку.
    ai_hint = rewrite_hint_with_ai(current_hint, game_state, CASE_DATA)
    # Нужно уменьшить game_state["hints_left"] на 1.
    game_state["hints_left"] -= 1
    # Нужно вывести подсказку.
    # Печатаем красивый заголовок подсказки.
    print_title("Подсказка")
    # Печатаем текст подсказки отдельной строкой.
    print(ai_hint)
    # Нужно вывести количество оставшихся подсказок.
    print()
    # Печатаем количество оставшихся подсказок как отдельное поле.
    print_field("Осталось подсказок", game_state["hints_left"])
    # Нужно вызвать wait_for_enter().
    # Пустую строку перед подсказкой Enter добавляет wait_for_enter().
    wait_for_enter()
