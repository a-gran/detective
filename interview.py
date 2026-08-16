# Берем данные дела из файла данных.
from data import CASE_DATA
# Берем вопросы для допроса из файла данных.
from data import INTERVIEW_QUESTIONS
from data import SUSPECTS
# Берем учебную функцию ответа персонажа из файла DeepSeek-клиента.
from deepseek_client import get_character_answer


# Создайте функцию, которая печатает линию-разделитель.
def print_separator():
    # Нужно вывести в консоль строку из 60 символов "-".
    print("-" * 60)


# Создайте функцию, которая ждет нажатия Enter.
def wait_for_enter():
    # Нужно вызвать input() с текстом вроде "Нажми Enter, чтобы продолжить...".
    input("\nНажми Enter, чтобы продолжить...")


# Создайте функцию, которая помогает выбрать подозреваемого.
def choose_suspect():
    # Нужно импортировать SUSPECTS из data.py или использовать готовый список подозреваемых.
    # Нужно показать список подозреваемых с номерами.
    print("\nВыберите подозреваемого")
    # Нужно вывести разделитель через print_separator().
    print_separator()
    for index, suspect in enumerate(SUSPECTS, start=1):
        # Нужно вывести номер, имя и роль подозреваемого.
        print(f"  {index}. {suspect['name']} - {suspect['role']}")

    # Нужно получить выбор игрока через input().
    # Нужно добавить пустую строку перед полем ввода.
    print()
    choice = input("Введите номер подозреваемого: ").strip()
    # Нужно вернуть выбранного подозреваемого или None.
    if not choice.isdigit():
        print("\nОшибка! Введите число.")
        return None

    index = int(choice) - 1
    if 0 <= index < len(SUSPECTS):
        return SUSPECTS[index]
    print("\nНеверный номер подозреваемого.")
    return None


# Создайте функцию, которая показывает вопросы для допроса.
def show_interview_questions():
    # Нужно пройти циклом по INTERVIEW_QUESTIONS.
    # Нужно вывести номер и текст каждого вопроса.
    # Нужно показать заголовок списка вопросов.
    print("\nДоступные вопросы")
    # Нужно вывести разделитель через print_separator().
    print_separator()
    for key, text in INTERVIEW_QUESTIONS.items():
        # Нужно вывести вопрос с отступом, чтобы список было легче читать.
        print(f"  {key}. {text}")
    # Нужно добавить пустую строку после списка вопросов.
    print()


# Создайте функцию, которая возвращает текст вопроса по номеру.
def get_question_text(question_key):
    # Нужно взять вопрос из INTERVIEW_QUESTIONS по ключу question_key.
    # Нужно вернуть текст вопроса через return.
    return INTERVIEW_QUESTIONS.get(question_key, "Вопрос не найден.")


# Создайте функцию, которая проводит допрос.
def interview_suspect(game_state):
    # Нужно проверить, остались ли вопросы в game_state["questions_left"].
    # Если вопросов нет, нужно показать сообщение и завершить функцию.
    if game_state["questions_left"] <= 0:
        print("\nУ вас не осталось вопросов!")
        wait_for_enter()
        return

    # Нужно показать заголовок "Допрос".
    print("\nДопрос")
    # Нужно вывести разделитель через print_separator().
    print_separator()
    # Нужно выбрать подозреваемого через choose_suspect().
    suspect = choose_suspect()
    # Если подозреваемый не выбран, нужно показать ошибку и завершить функцию.
    if suspect is None:
        print("\nДопрос отменен.")
        wait_for_enter()
        return
    # Нужно показать вопросы через show_interview_questions().
    show_interview_questions()
    # Нужно получить номер вопроса через input().
    question_key = input("Выберите номер вопроса: ").strip()
    # Нужно проверить, есть ли такой ответ в suspect["answers"].
    if question_key not in suspect["answers"]:
        print("\nНа этот вопрос нет ответа.")
        wait_for_enter()
        return
    # Нужно получить текст вопроса через get_question_text().
    question_text = get_question_text(question_key)

    # Нужно получить ответ через get_character_answer().
    answer = get_character_answer(suspect, question_key, question_text, CASE_DATA)
    # Нужно уменьшить game_state["questions_left"] на 1.
    game_state["questions_left"] -= 1
    # Нужно добавить запись в game_state["question_history"].
    game_state["question_history"].append(f"[{suspect['name']}] Вопрос: {question_text}\nОтвет: {answer}")
    # Нужно вывести ответ подозреваемого.
    # Нужно добавить пустую строку перед ответом.
    print()
    # Нужно показать, какой подозреваемый отвечает.
    print(f"{suspect['name']} отвечает")
    # Нужно вывести разделитель перед ответом.
    print_separator()
    # Нужно вывести сам ответ подозреваемого.
    print(answer)
    # Нужно вызвать wait_for_enter().
    wait_for_enter()


# Проверяем, что файл запущен напрямую.
if __name__ == "__main__":
    # Печатаем название проверки для ученика.
    print("Проверка файла interview.py")
    # Создаем тестовое состояние игры.
    test_state = {"questions_left": 3, "question_history": []}
    # Пытаемся проверить функции допроса отдельно.
    try:
        # Запускаем полный тест допроса.
        interview_suspect(test_state)
        # Печатаем состояние после допроса.
        print(test_state)
    # Ловим ошибку, если функция еще не реализована.
    except NotImplementedError as error:
        # Печатаем понятное сообщение для ученика.
        print(f"Нужно доделать задание: {error}")
