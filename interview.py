# Берем данные дела из файла данных.
from data import CASE_DATA
# Берем вопросы для допроса из файла данных.
from data import INTERVIEW_QUESTIONS
# Берем учебную функцию ответа персонажа из файла DeepSeek-клиента.
from deepseek_client import get_character_answer


# Создайте функцию, которая печатает линию-разделитель.
def print_separator():
    # Нужно вывести в консоль строку из 60 символов "-".
    raise NotImplementedError("Команда 2 должна реализовать print_separator в interview.py")


# Создайте функцию, которая ждет нажатия Enter.
def wait_for_enter():
    # Нужно вызвать input() с текстом вроде "Нажми Enter, чтобы продолжить...".
    raise NotImplementedError("Команда 2 должна реализовать wait_for_enter в interview.py")


# Создайте функцию, которая помогает выбрать подозреваемого.
def choose_suspect():
    # Нужно импортировать SUSPECTS из data.py или использовать готовый список подозреваемых.
    # Нужно показать список подозреваемых с номерами.
    # Нужно получить выбор игрока через input().
    # Нужно вернуть выбранного подозреваемого или None.
    raise NotImplementedError("Команда 2 должна реализовать choose_suspect в interview.py")


# Создайте функцию, которая показывает вопросы для допроса.
def show_interview_questions():
    # Нужно пройти циклом по INTERVIEW_QUESTIONS.
    # Нужно вывести номер и текст каждого вопроса.
    raise NotImplementedError("Команда 2 должна реализовать show_interview_questions в interview.py")


# Создайте функцию, которая возвращает текст вопроса по номеру.
def get_question_text(question_key):
    # Нужно взять вопрос из INTERVIEW_QUESTIONS по ключу question_key.
    # Нужно вернуть текст вопроса через return.
    raise NotImplementedError("Команда 2 должна реализовать get_question_text в interview.py")


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
    raise NotImplementedError("Команда 2 должна реализовать interview_suspect в interview.py")


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
