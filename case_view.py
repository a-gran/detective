# Берем данные дела из файла данных.
from data import CASE_DATA


# Создайте функцию, которая печатает линию-разделитель.
def print_separator():
    # Нужно вывести в консоль строку из 60 символов "-".
    raise NotImplementedError("Команда 2 должна реализовать print_separator в case_view.py")


# Создайте функцию, которая ждет нажатия Enter.
def wait_for_enter():
    # Нужно вызвать input() с текстом вроде "Нажми Enter, чтобы продолжить...".
    raise NotImplementedError("Команда 2 должна реализовать wait_for_enter в case_view.py")


# Создайте функцию, которая показывает описание дела.
def show_case_description():
    # Нужно вывести название дела из CASE_DATA["title"].
    # Нужно вывести разделитель через print_separator().
    # Нужно вывести описание дела из CASE_DATA["description"].
    # Нужно вызвать wait_for_enter(), чтобы игрок успел прочитать дело.
    raise NotImplementedError("Команда 2 должна реализовать show_case_description в case_view.py")


# Проверяем, что файл запущен напрямую.
if __name__ == "__main__":
    # Печатаем название проверки для ученика.
    print("Проверка файла case_view.py")
    # Пытаемся показать описание дела отдельно.
    try:
        # Запускаем функцию показа дела.
        show_case_description()
    # Ловим ошибку, если функция еще не реализована.
    except NotImplementedError as error:
        # Печатаем понятное сообщение для ученика.
        print(f"Нужно доделать задание: {error}")
