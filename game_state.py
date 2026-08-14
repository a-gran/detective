# Берем действия меню расследования из файла данных.
from data import GAME_ACTIONS


# Создайте функцию, которая печатает линию-разделитель.
def print_separator():
    # Нужно вывести в консоль строку из 60 символов "-".
    print("-" * 60)


# Создайте функцию, которая ждет нажатия Enter.
def wait_for_enter():
    # Нужно вызвать input() с текстом вроде "Нажми Enter, чтобы продолжить...".
    input("Нажми Enter, чтобы продолжить...")


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
    # Нужно показать выбранную сложность из game_state["difficulty"].
    print(f"\nРасследование. Сложность: {game_state['difficulty']}")
    # Нужно показать количество вопросов из game_state["questions_left"].
    print(f"Вопросы: {game_state['questions_left']}")
    # Нужно показать количество подсказок из game_state["hints_left"].
    print(f"Подсказки: {game_state['hints_left']}")
    # Нужно вывести разделитель через print_separator().
    print_separator()
    # Нужно пройти циклом по GAME_ACTIONS и показать все действия.
    for action_key, action_text in GAME_ACTIONS.items():
        print(f"{action_key}. {action_text}")
    # Нужно получить выбор игрока через input().
    print()
    choice = input("Выбери действие: ").strip()
    # Нужно вернуть выбор игрока через return.
    return choice


# Создайте функцию, которая показывает историю допросов.
def show_history(game_state):
    # Нужно вывести заголовок "История допросов".
    print("\nИстория допросов")
    # Нужно вывести разделитель через print_separator().
    print_separator()
    # Нужно проверить список game_state["question_history"].
    if not game_state["question_history"]:
    # Если список пустой, нужно написать, что игрок еще никого не допрашивал.
        print("Ты еще никого не допрашивал.")
    # Если список не пустой, нужно циклом вывести каждую запись.
    else:
        for record in game_state["question_history"]:
            print(f"- {record}")
    # Нужно вызвать wait_for_enter(), чтобы игрок успел прочитать историю.
    print()
    wait_for_enter()


# Проверяем, что файл запущен напрямую.
if __name__ == "__main__":
    # Печатаем название проверки для ученика.
    print("Проверка файла game_state.py")
    # Создаем тестовую сложность, чтобы не ждать готового difficulty.py.
    test_difficulty = {"name": "Тест", "questions": 3, "hints": 1}
    # Пытаемся проверить функции этого файла.
    try:
        # Создаем тестовое состояние игры.
        test_state = create_game_state(test_difficulty)
        # Печатаем созданное состояние.
        print(test_state)
        # Показываем историю на тестовом состоянии.
        show_history(test_state)
        # Показываем меню расследования на тестовом состоянии.
        choice = show_game_menu(test_state)
        # Печатаем выбор игрока.
        print(f"Выбран пункт: {choice}")
    # Ловим ошибку, если функция еще не реализована.
    except NotImplementedError as error:
        # Печатаем понятное сообщение для ученика.
        print(f"Нужно доделать задание: {error}")
