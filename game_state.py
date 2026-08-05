# Берем действия меню расследования из файла данных.
from data import GAME_ACTIONS


# Создайте функцию, которая печатает линию-разделитель.
def print_separator():
    # Нужно вывести в консоль строку из 60 символов "-".
    raise NotImplementedError("Команда 1 должна реализовать print_separator в game_state.py")


# Создайте функцию, которая ждет нажатия Enter.
def wait_for_enter():
    # Нужно вызвать input() с текстом вроде "Нажми Enter, чтобы продолжить...".
    raise NotImplementedError("Команда 1 должна реализовать wait_for_enter в game_state.py")


# Создайте функцию, которая делает новое состояние игры.
def create_game_state(difficulty):
    # Нужно создать словарь с данными игрока.
    # В словаре должны быть ключи "difficulty", "questions_left", "hints_left", "viewed_clues", "question_history".
    # В "difficulty" нужно сохранить difficulty["name"].
    # В "questions_left" нужно сохранить difficulty["questions"].
    # В "hints_left" нужно сохранить difficulty["hints"].
    # В "viewed_clues" нужно сохранить пустой список.
    # В "question_history" нужно сохранить пустой список.
    # Нужно вернуть этот словарь через return.
    raise NotImplementedError("Команда 1 должна реализовать create_game_state в game_state.py")


# Создайте функцию, которая показывает меню расследования.
def show_game_menu(game_state):
    # Нужно показать выбранную сложность из game_state["difficulty"].
    # Нужно показать количество вопросов из game_state["questions_left"].
    # Нужно показать количество подсказок из game_state["hints_left"].
    # Нужно вывести разделитель через print_separator().
    # Нужно пройти циклом по GAME_ACTIONS и показать все действия.
    # Нужно получить выбор игрока через input().
    # Нужно вернуть выбор игрока через return.
    raise NotImplementedError("Команда 1 должна реализовать show_game_menu в game_state.py")


# Создайте функцию, которая показывает историю допросов.
def show_history(game_state):
    # Нужно вывести заголовок "История допросов".
    # Нужно вывести разделитель через print_separator().
    # Нужно проверить список game_state["question_history"].
    # Если список пустой, нужно написать, что игрок еще никого не допрашивал.
    # Если список не пустой, нужно циклом вывести каждую запись.
    # Нужно вызвать wait_for_enter(), чтобы игрок успел прочитать историю.
    raise NotImplementedError("Команда 1 должна реализовать show_history в game_state.py")


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
