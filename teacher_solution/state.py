# Берем функцию AI-резюме истории допросов.
from ai_client import summarize_history_with_ai
# Берем действия меню расследования из файла данных.
from data import CASE_DATA, GAME_ACTIONS

# Берем общие функции для ввода, красивого вывода состояния игры и ожидания Enter.
from ui_helpers import ask_option, print_field, print_option, print_title, wait_for_enter


# Создайте функцию, которая делает новое состояние игры.
def create_game_state(difficulty):
    # Нужно создать словарь с данными игрока.
    game_state = {
        # В словаре должны быть ключи "difficulty", "questions_left", "hints_left", "viewed_clues", "question_history".
        # В "difficulty" нужно сохранить difficulty["name"].
        "difficulty": difficulty["name"],
        # В "questions_left" нужно сохранить difficulty["questions"].
        "questions_left": difficulty["questions"],
        # В "hints_left" нужно сохранить difficulty["hints"].
        "hints_left": difficulty["hints"],
        # В "viewed_clues" нужно сохранить пустой список.
        "viewed_clues": [],
        # В "question_history" нужно сохранить пустой список.
        "question_history": [],
    }
    # Нужно вернуть этот словарь через return.
    return game_state


# Создайте функцию, которая показывает меню расследования.
def show_game_menu(game_state):
    # Печатаем красивый заголовок меню расследования.
    print_title("Расследование")
    # Показываем выбранную сложность из game_state["difficulty"].
    print_field("Сложность", game_state["difficulty"])
    # Показываем количество вопросов из game_state["questions_left"].
    print_field("Вопросы", game_state["questions_left"])
    # Показываем количество подсказок из game_state["hints_left"].
    print_field("Подсказки", game_state["hints_left"])
    # Добавляем пустую строку перед списком действий.
    print()
    # Нужно пройти циклом по GAME_ACTIONS и показать все действия.
    for action_key, action_text in GAME_ACTIONS.items():
        # Печатаем действие как пункт меню.
        print_option(action_key, action_text)
    # Нужно получить выбор игрока через input().
    print()
    choice = ask_option(
        GAME_ACTIONS,
        "Выбери действие: ",
        "Такого пункта нет. Попробуй еще раз.",
    )
    # Нужно вернуть выбор игрока через return.
    return choice


# Создайте функцию, которая показывает историю допросов.
def show_history(game_state):
    # Печатаем красивый заголовок истории допросов.
    print_title("История допросов")
    # Нужно проверить список game_state["question_history"].
    if not game_state["question_history"]:
        # Если список пустой, нужно написать, что игрок еще никого не допрашивал.
        print("Ты еще никого не допрашивал.")
    # Если список не пустой, нужно циклом вывести каждую запись.
    else:
        # Проходим по истории допросов вместе с номером записи.
        for index, record in enumerate(game_state["question_history"], start=1):
            # Печатаем номер записи и имя подозреваемого.
            print_option(index, record["suspect"])
            # Печатаем вопрос игрока отдельным полем.
            print_field("Вопрос", record["question"])
            # Печатаем ответ подозреваемого отдельным полем.
            print_field("Ответ", record["answer"])
            # Добавляем пустую строку между записями истории.
            print()
        # Просим AI кратко пересказать уже существующую историю допросов.
        summary = summarize_history_with_ai(game_state, CASE_DATA)
        # Печатаем отдельный заголовок для AI-резюме.
        print_title("Краткое резюме AI")
        # Печатаем AI-резюме без изменения истории и состояния игры.
        print(summary)
    # Нужно вызвать wait_for_enter(), чтобы игрок успел прочитать историю.
    # Пустую строку перед подсказкой Enter добавляет wait_for_enter().
    wait_for_enter()
