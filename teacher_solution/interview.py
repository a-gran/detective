# Берем данные дела из файла данных.
from data import CASE_DATA
# Берем список подозреваемых из файла данных.
from data import SUSPECTS
# Берем вопросы для допроса из файла данных.
from data import INTERVIEW_QUESTIONS
# Берем учебную функцию ответа персонажа из файла DeepSeek-клиента.
from deepseek_client import get_character_answer


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


# Создаем функцию, которая показывает вопросы для допроса.
def show_interview_questions():
    # Перебираем все вопросы вместе с их номерами.
    for question_key, question_text in INTERVIEW_QUESTIONS.items():
        # Печатаем номер и текст вопроса.
        print(f"{question_key}. {question_text}")


# Создаем функцию, которая возвращает текст вопроса по номеру.
def get_question_text(question_key):
    # Возвращаем текст вопроса из словаря вопросов.
    return INTERVIEW_QUESTIONS[question_key]


# Создаем функцию, которая проводит допрос.
def interview_suspect(game_state):
    # Проверяем, остались ли у игрока вопросы.
    if game_state["questions_left"] <= 0:
        # Сообщаем, что вопросы закончились.
        print("\nВопросы закончились. Пора делать выводы.")
        # Ждем, пока игрок прочитает сообщение.
        wait_for_enter()
        # Завершаем функцию.
        return
    # Печатаем заголовок допроса.
    print("\nДопрос")
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
        # Завершаем функцию.
        return
    # Показываем вопросы для допроса.
    show_interview_questions()
    # Получаем выбранный вопрос.
    question = input("Выбери вопрос: ").strip()
    # Проверяем, есть ли такой ответ у подозреваемого.
    if question not in suspect["answers"]:
        # Сообщаем об ошибке выбора вопроса.
        print("Такого вопроса нет.")
        # Ждем, пока игрок прочитает сообщение.
        wait_for_enter()
        # Завершаем функцию.
        return
    # Получаем текст выбранного вопроса.
    question_text = get_question_text(question)
    # Получаем ответ подозреваемого через учебную точку подключения DeepSeek.
    answer, prompt = get_character_answer(suspect, question, question_text, CASE_DATA)
    # Уменьшаем количество оставшихся вопросов.
    game_state["questions_left"] -= 1
    # Добавляем запись в историю допросов.
    game_state["question_history"].append(f"{suspect['name']}: {answer}")
    # Печатаем имя подозреваемого и ответ.
    print(f"\n{suspect['name']}: {answer}")
    # Печатаем количество оставшихся вопросов.
    print(f"Осталось вопросов: {game_state['questions_left']}")
    # Ждем, пока игрок прочитает ответ.
    wait_for_enter()


# Проверяем, что файл запущен напрямую.
if __name__ == "__main__":
    # Печатаем название проверки.
    print("Проверка файла interview.py")
    # Создаем тестовое состояние игры.
    test_state = {"questions_left": 3, "question_history": []}
    # Показываем вопросы для допроса.
    show_interview_questions()
    # Если есть вопрос с номером "1", печатаем его текст.
    if "1" in INTERVIEW_QUESTIONS:
        # Печатаем текст первого вопроса.
        print(get_question_text("1"))
    # Запускаем полный тест допроса.
    interview_suspect(test_state)
    # Печатаем состояние после допроса.
    print(test_state)
