# Берем данные дела из файла данных.
from data import CASE_DATA
# Берем вопросы для допроса из файла данных.
from data import INTERVIEW_QUESTIONS
# Берем учебную функцию ответа персонажа из файла DeepSeek-клиента.
from deepseek_client import get_character_answer


# Создайте функцию, которая печатает линию-разделитель.
def print_separator():
    # Нужно вывести в консоль строку из 60 символов "-".
    print("-"*60)


# Создайте функцию, которая ждет нажатия Enter.
def wait_for_enter():
    # Нужно вызвать input() с текстом вроде "Нажми Enter, чтобы продолжить...".
    input("Чтобы продолжить раскрывать дело, нажмите Enter")


# Создайте функцию, которая помогает выбрать подозреваемого.
def choose_suspect():
    # Нужно импортировать SUSPECTS из data.py или использовать готовый список подозреваемых.
    # Нужно показать список подозреваемых с номерами.
    # Нужно получить выбор игрока через input().
    # Нужно вернуть выбранного подозреваемого или None.
    from data import SUSPECTS
    print("Подозреваемые")
    print_separator()
    for i, suspect in enumerate(SUSPECTS, 1):
        print(f"{i}. {suspect['name']}")
        print(f"   Роль: {suspect['role']}")
        print(f"   Характер: {suspect['personality']}")
        print(f"   Алиби: {suspect['alibi']}")
        print()

    answer = input("Выберите номер подозреваемого: ")
    if not answer.isdigit():
        print("Ошибка! Введите число.")
        return None

    index = int(answer) - 1
    if index < 0 or index >= len(SUSPECTS):
        print("Неверный номер!")
        return None

    return SUSPECTS[index]


# Создайте функцию, которая показывает вопросы для допроса.
def show_interview_questions():
    # Нужно пройти циклом по INTERVIEW_QUESTIONS.
    # Нужно вывести номер и текст каждого вопроса.
    print("\nДоступные вопросы:")
    for key, question in INTERVIEW_QUESTIONS.items():
        print(f"{key}. {question}")


# Создайте функцию, которая возвращает текст вопроса по номеру.
def get_question_text(question_key):
    # Нужно взять вопрос из INTERVIEW_QUESTIONS по ключу question_key.
    # Нужно вернуть текст вопроса через return.
    if question_key in INTERVIEW_QUESTIONS:
        return INTERVIEW_QUESTIONS[question_key]
    else:
        return "Вопрос не найден"


# Создайте функцию, которая проводит допрос.
def interview_suspect(game_state):
    # Нужно проверить, остались ли вопросы в game_state["questions_left"].
    # Если вопросов нет, нужно показать сообщение и завершить функцию.
    # Нужно показать заголовок "Допрос".
    # Нужно вывести разделитель через print_separator().
    # Нужно выбрать подозреваемого через choose_suspect().
    # Если подозреваемый не выбран, нужно показать ошибку и завершить функцию.
    # Нужно показать вопросы через show_interview_questions().
    # Нужно получить номер вопроса через input().
    # Нужно проверить, есть ли такой ответ в suspect["answers"].
    # Нужно получить текст вопроса через get_question_text().
    # Нужно получить ответ через get_character_answer().
    # Нужно уменьшить game_state["questions_left"] на 1.
    # Нужно добавить запись в game_state["question_history"].
    # Нужно вывести ответ подозреваемого.
    # Нужно вызвать wait_for_enter().

    # Проверяем, остались ли вопросы
    if game_state["questions_left"] <= 0:
        print("У вас закончились вопросы.")
        wait_for_enter()
        return

    print("\nДопрос")
    print_separator()

    # Выбираем подозреваемого
    suspect = choose_suspect()
    if suspect is None:
        print("Вы не выбрали подозреваемого")
        wait_for_enter()
        return

    print(f"\nВы допрашиваете: {suspect['name']}")
    print_separator()

    # Показываем доступные вопросы
    show_interview_questions()

    # Получаем номер вопроса
    question_key = input("\nВведите номер вопроса: ")

    # Проверяем, есть ли такой вопрос у подозреваемого
    if question_key not in suspect["answers"]:
        print("Такого вопроса нет в списке!")
        wait_for_enter()
        return

    # Получаем текст вопроса и ответ
    question_text = get_question_text(question_key)
    answer = suspect["answers"][question_key]

    # Уменьшаем количество оставшихся вопросов
    game_state["questions_left"] -= 1

    # Добавляем запись в историю
    game_state["question_history"].append({
        "suspect": suspect["name"],
        "question": question_text,
        "answer": answer
    })

    # Выводим ответ
    print(f"\n{suspect['name']}: {answer}")
    print(f"Осталось вопросов: {game_state['questions_left']}")

    wait_for_enter()


# Проверяем, что файл запущен напрямую.
if __name__ == "__main__":
    # Печатаем название проверки для ученика.
    print("Проверка файла interview.py")
    # Создаем тестовое состояние игры.
    test_state = {"questions_left": 3, "question_history": []}
    # Пытаемся проверить функции допроса отдельно.
    try:
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
    # Ловим ошибку, если функция еще не реализована.
    except NotImplementedError as error:
        # Печатаем понятное сообщение для ученика.
        print(f"Нужно доделать задание: {error}")
