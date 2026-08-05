# Берем список улик из файла данных.
from data import CLUES


# Создаем локальную функцию, которая печатает линию-разделитель.
def print_separator():
    # Печатаем строку из 60 символов "-".
    print("-" * 60)


# Создаем локальную функцию, которая ждет нажатия Enter.
def wait_for_enter():
    # Просим игрока нажать Enter, чтобы он успел прочитать текст.
    input("\nНажми Enter, чтобы продолжить...")


# Создаем функцию, которая показывает улики.
def show_clues(game_state):
    # Печатаем заголовок улик.
    print("\nУлики")
    # Печатаем разделитель.
    print_separator()
    # Перебираем все улики вместе с номером.
    for index, clue in enumerate(CLUES, start=1):
        # Печатаем название улики.
        print(f"{index}. {clue['title']}")
        # Печатаем описание улики.
        print(f"   {clue['description']}")
        # Проверяем, есть ли улика в списке изученных.
        if clue["title"] not in game_state["viewed_clues"]:
            # Добавляем название улики в список изученных.
            game_state["viewed_clues"].append(clue["title"])
    # Ждем, пока игрок прочитает улики.
    wait_for_enter()


# Проверяем, что файл запущен напрямую.
if __name__ == "__main__":
    # Печатаем название проверки.
    print("Проверка файла clues_view.py")
    # Создаем тестовое состояние игры.
    test_state = {"viewed_clues": []}
    # Показываем улики.
    show_clues(test_state)
    # Печатаем состояние после просмотра улик.
    print(test_state)
