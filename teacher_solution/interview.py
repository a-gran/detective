# Берем учебную функцию ответа персонажа из файла AI-клиента.
from ai_client import get_character_answer

# Берем данные дела и вопросы для допроса из файла данных.
from data import CASE_DATA, INTERVIEW_QUESTIONS, SUSPECTS

# Берем общие функции для ввода, красивого вывода допроса и ожидания Enter.
from ui_helpers import (
    ask_number,
    ask_option,
    print_field,
    print_option,
    print_title,
    wait_for_enter,
)


# Создайте функцию, которая помогает выбрать подозреваемого.
def choose_suspect():
    # Нужно импортировать SUSPECTS из data.py или использовать готовый список подозреваемых.
    # Нужно показать список подозреваемых с номерами.
    # Нужно получить выбор игрока через input().
    # Нужно вернуть выбранного подозреваемого или None.
    # Печатаем красивый заголовок списка подозреваемых.
    print_title("Подозреваемые")
    for i, suspect in enumerate(SUSPECTS, 1):
        # Печатаем имя подозреваемого как пункт списка.
        print_option(i, suspect["name"])
        # Печатаем роль подозреваемого отдельным полем.
        print_field("Роль", suspect["role"])
        # Печатаем характер подозреваемого отдельным полем.
        print_field("Характер", suspect["personality"])
        # Печатаем алиби подозреваемого отдельным полем.
        print_field("Алиби", suspect["alibi"])
        print()

    index = ask_number(len(SUSPECTS), "Выберите номер подозреваемого: ")
    return SUSPECTS[index]


# Создайте функцию, которая показывает вопросы для допроса.
def show_interview_questions():
    # Нужно пройти циклом по INTERVIEW_QUESTIONS.
    # Нужно вывести номер и текст каждого вопроса.
    # Печатаем красивый заголовок списка вопросов.
    print_title("Доступные вопросы")
    for key, question in INTERVIEW_QUESTIONS.items():
        # Печатаем вопрос как пункт списка.
        print_option(key, question)


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

    # Печатаем красивый заголовок раздела допроса.
    print_title("Допрос")

    # Выбираем подозреваемого
    suspect = choose_suspect()
    # Печатаем имя выбранного подозреваемого отдельным заголовком.
    print_title(f"Вы допрашиваете: {suspect['name']}")

    # Показываем доступные вопросы
    show_interview_questions()

    # Получаем номер вопроса
    question_key = ask_option(
        suspect["answers"],
        "\nВведите номер вопроса: ",
        "Такого вопроса нет в списке!",
    )

    # Получаем текст вопроса.
    question_text = get_question_text(question_key)
    # Получаем ответ через Groq или готовый запасной ответ.
    answer, prompt = get_character_answer(
        suspect, question_key, question_text, CASE_DATA
    )

    # Уменьшаем количество оставшихся вопросов
    game_state["questions_left"] -= 1

    # Добавляем запись в историю
    game_state["question_history"].append(
        {
            "suspect": suspect["name"],
            "question": question_text,
            "answer": answer,
            "prompt": prompt,
        }
    )

    # Выводим ответ
    # Добавляем пустую строку перед ответом, чтобы он отделялся от выбора вопроса.
    print()
    # Печатаем ответ подозреваемого как поле с именем.
    print_field(suspect["name"], answer)
    # Печатаем количество оставшихся вопросов отдельным полем.
    print_field("Осталось вопросов", game_state["questions_left"])

    wait_for_enter()
