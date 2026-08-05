# Архитектура teacher_solution

`teacher_solution/` повторяет архитектуру ученического проекта.

```text
teacher_solution/
├── main.py
├── data.py
├── deepseek_client.py
├── main_menu.py
├── difficulty.py
├── game_state.py
├── final.py
├── case_view.py
├── suspects_view.py
├── clues_view.py
├── interview.py
├── hints.py
└── docs/
```

## Принцип

В корне проекта лежит версия для учеников.

В `teacher_solution/` лежит такая же плоская структура, но с готовым кодом.

Это позволяет проверять работу учеников по тем же именам файлов, функций и переменных.

## Независимая проверка

Каждый файл решения содержит маленькую проверку в блоке `if __name__ == "__main__"`.

Например:

```bash
python hints.py
```
