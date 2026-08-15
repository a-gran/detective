# Берем список подозреваемых из файла данных.
from data import SUSPECTS


# Создайте функцию, которая печатает линию-разделитель.
def print_separator():
    # Нужно вывести в консоль строку из 60 символов "-".
    print("-"*60)
    #raise NotImplementedError("Команда 2 должна реализовать print_separator в suspects.py")


# Создайте функцию, которая ждет нажатия Enter.
def wait_for_enter():
    # Нужно вызвать input() с текстом вроде "Нажми Enter, чтобы продолжить...".
    input("Чтобы продолжить раскрывать дело,нажмите Enter")
    #raise NotImplementedError("Команда 2 должна реализовать wait_for_enter в suspects.py")


# Создайте функцию, которая показывает подозреваемых.
def show_suspects():
    # Нужно вывести заголовок "Подозреваемые".
    # Нужно вывести разделитель через print_separator().
    # Нужно пройти циклом по SUSPECTS.
    # Для каждого подозреваемого нужно вывести номер, имя, роль, характер и алиби.
    # Нужно вызвать wait_for_enter(), чтобы игрок успел прочитать список.
    print("Подозреваемые")
    print_separator()
    for i, clue in enumerate(SUSPECTS,1):
        print(f"{i}. {clue['name']}")
        print(f"   {clue['role']}")
        print(f"   {clue['personality']}")
        print(f"   {clue['alibi']}")
    print()
    wait_for_enter()
    #raise NotImplementedError("Команда 2 должна реализовать show_suspects в suspects.py")


# Создайте функцию, которая помогает выбрать подозреваемого.
def choose_suspect():
    # Нужно показать список подозреваемых с номерами.
    # Нужно получить выбор игрока через input().
    # Нужно проверить, что игрок ввел число.
    # Нужно превратить номер в индекс списка.
    # Если индекс правильный, нужно вернуть выбранного подозреваемого.
    # Если выбор неправильный, нужно вернуть None.
    for i, clue in enumerate(SUSPECTS,1):
        print(f"{i}. {clue['name']}")
    answer = input("Кто из них подозреваемый?:")
    if not answer.isdigit():
        return None
    index = int(answer) - 1
    if index < 0 or index > len(SUSPECTS):
        return None
    else:
        return SUSPECTS[index]
    #raise NotImplementedError("Команда 2 должна реализовать choose_suspect в suspects.py")


# Проверяем, что файл запущен напрямую.
if __name__ == "__main__":
    # Печатаем название проверки для ученика.
    print("Проверка файла suspects.py")
    # Пытаемся проверить функции этого файла.
    try:
        # Показываем подозреваемых.
        show_suspects()
        # Просим выбрать подозреваемого.
        suspect = choose_suspect()
        # Печатаем выбранного подозреваемого.
        print(f"Выбран подозреваемый: {suspect}")
    # Ловим ошибку, если функция еще не реализована.
    except NotImplementedError as error:
        # Печатаем понятное сообщение для ученика.
        print(f"Нужно доделать задание: {error}")
