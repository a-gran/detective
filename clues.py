# Берем список улик из файла данных.
from data import CLUES


# Создайте функцию, которая печатает линию-разделитель.
def print_separator():
    # Нужно вывести в консоль строку из 60 символов "-".
    print("-" * 60)


# Создайте функцию, которая ждет нажатия Enter.
def wait_for_enter():
    # Нужно вызвать input() с текстом вроде "Нажми Enter, чтобы продолжить...".
    input("Нажми Enter, чтобы продолжить...")


# Создайте функцию, которая показывает улики.
def show_clues(game_state):
    # Нужно вывести заголовок "Улики".
    print("Улики")
    # Нужно вывести разделитель через print_separator().
    print_separator()
    # Нужно пройти циклом по CLUES.
    for index, clue in enumerate(CLUES, start=1):
    # Для каждой улики нужно вывести номер, название и описание.
        print(f"{index}. {clue['title']}")
        print(f"   {clue['description']}")
    # Нужно добавлять название изученной улики в game_state["viewed_clues"].
        if clue["title"] not in game_state["viewed_clues"]:
            game_state["viewed_clues"].append(clue["title"])
    # Нужно вызвать wait_for_enter(), чтобы игрок успел прочитать улики.
    print()
    wait_for_enter()


# Проверяем, что файл запущен напрямую.
if __name__ == "__main__":
    # Печатаем название проверки для ученика.
    print("Проверка файла clues.py")
    # Создаем тестовое состояние игры.
    test_state = {"viewed_clues": []}
    # Пытаемся показать улики отдельно.
    try:
        # Запускаем функцию показа улик.
        show_clues(test_state)
        # Печатаем состояние после просмотра улик.
        print(test_state)
    # Ловим ошибку, если функция еще не реализована.
    except NotImplementedError as error:
        # Печатаем понятное сообщение для ученика.
        print(f"Нужно доделать задание: {error}")
