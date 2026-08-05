# Берем данные дела из файла данных.
from data import CASE_DATA
# Берем финальные тексты из файла данных.
from data import RESULT_TEXTS
# Берем список подозреваемых из файла данных.
from data import SUSPECTS
# Берем учебную функцию анализа версии игрока.
from deepseek_client import analyze_player_version


# Создаем локальную функцию, которая печатает линию-разделитель.
def print_separator():
    # Печатаем строку из 60 символов "-".
    print("-" * 60)


# Создаем локальную функцию, которая ждет нажатия Enter.
def wait_for_enter():
    # Просим игрока нажать Enter, чтобы он успел прочитать текст.
    input("\nНажми Enter, чтобы продолжить...")


# Создаем локальную функцию, которая помогает выбрать подозреваемого.
def choose_suspect():
    # Перебираем всех подозреваемых вместе с номером.
    for index, suspect in enumerate(SUSPECTS, start=1):
        # Печатаем номер и имя подозреваемого.
        print(f"{index}. {suspect['name']}")
    # Получаем выбор игрока.
    choice = input("Выбери подозреваемого: ").strip()
    # Проверяем, является ли выбор числом.
    if not choice.isdigit():
        # Возвращаем None, если игрок ввел не число.
        return None
    # Превращаем номер игрока в индекс списка.
    suspect_index = int(choice) - 1
    # Проверяем, находится ли индекс внутри списка подозреваемых.
    if 0 <= suspect_index < len(SUSPECTS):
        # Возвращаем выбранного подозреваемого.
        return SUSPECTS[suspect_index]
    # Возвращаем None, если номер неправильный.
    return None


# Создаем функцию, которая проводит финальное обвинение.
def make_accusation():
    # Печатаем заголовок финала.
    print("\nФинальное обвинение")
    # Печатаем разделитель.
    print_separator()
    # Просим игрока выбрать подозреваемого.
    suspect = choose_suspect()
    # Проверяем, выбран ли подозреваемый.
    if suspect is None:
        # Сообщаем об ошибке выбора.
        print("Такого подозреваемого нет.")
        # Ждем, пока игрок прочитает сообщение.
        wait_for_enter()
        # Возвращаем False, потому что игра не завершилась.
        return False
    # Просим игрока объяснить свою версию.
    version = input("Объясни свою версию: ").strip()
    # Печатаем разделитель.
    print_separator()
    # Проверяем, совпадает ли имя выбранного подозреваемого с преступником.
    if suspect["name"].lower() == CASE_DATA["criminal"].lower():
        # Показываем сообщение для правильного ответа.
        print(RESULT_TEXTS["correct"])
    # Если имя не совпало, показываем сообщение для ошибки.
    else:
        # Показываем сообщение для неправильного ответа.
        print(RESULT_TEXTS["wrong"])
    # Показываем версию игрока.
    print(f"\n{RESULT_TEXTS['player_version_label']}: {version}")
    # Показываем правильное объяснение.
    print(f"\n{RESULT_TEXTS['solution_label']}: {CASE_DATA['solution']}")
    # Получаем учебный комментарий помощника.
    assistant_comment = analyze_player_version(version, suspect["name"], CASE_DATA)
    # Показываем учебный комментарий помощника.
    print(assistant_comment)
    # Ждем, пока игрок прочитает финал.
    wait_for_enter()
    # Возвращаем True, потому что партия закончилась.
    return True


# Проверяем, что файл запущен напрямую.
if __name__ == "__main__":
    # Печатаем название проверки.
    print("Проверка файла final.py")
    # Запускаем финальное обвинение.
    result = make_accusation()
    # Печатаем результат функции.
    print(f"Функция вернула: {result}")
