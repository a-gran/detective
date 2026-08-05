# Берем настройки сложности из файла данных.
from data import DIFFICULTY_SETTINGS


# Создаем локальную функцию, которая печатает линию-разделитель.
def print_separator():
    # Печатаем строку из 60 символов "-".
    print("-" * 60)


# Создаем функцию, которая просит игрока выбрать сложность.
def choose_difficulty():
    # Запускаем цикл, пока игрок не выберет правильный вариант.
    while True:
        # Печатаем заголовок выбора сложности.
        print("\nВыбор сложности")
        # Печатаем разделитель.
        print_separator()
        # Перебираем все уровни сложности.
        for difficulty_key, difficulty_data in DIFFICULTY_SETTINGS.items():
            # Печатаем номер, название и описание сложности.
            print(f"{difficulty_key}. {difficulty_data['name']}: {difficulty_data['description']}")
        # Получаем выбор игрока.
        choice = input("Выбери сложность: ").strip()
        # Проверяем, есть ли такой ключ в настройках сложности.
        if choice in DIFFICULTY_SETTINGS:
            # Возвращаем выбранную сложность.
            return DIFFICULTY_SETTINGS[choice]
        # Сообщаем игроку, что выбор неправильный.
        print("Такого варианта нет. Попробуй еще раз.")


# Проверяем, что файл запущен напрямую.
if __name__ == "__main__":
    # Печатаем название проверки.
    print("Проверка файла difficulty.py")
    # Запускаем функцию выбора сложности.
    selected_difficulty = choose_difficulty()
    # Печатаем подпись результата.
    print("Функция вернула:")
    # Печатаем выбранную сложность.
    print(selected_difficulty)
