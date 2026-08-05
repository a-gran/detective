# Основные команды Git

Эта инструкция помогает понять, какие Git-команды нужны чаще всего, какие флаги у них используются и в каком порядке их выполнять.

Главное правило: Git-команды часто зависят от правильной последовательности. Если поменять порядок, можно получить ошибку или отправить не те изменения.

---

# 1. Настройка Git

## Посмотреть настройки

```bash
git config --list
```

Команда показывает текущие настройки Git.

## Указать имя пользователя

```bash
git config --global user.name "Ваше Имя"
```

Флаг `--global` значит, что настройка применяется ко всем Git-проектам на компьютере.

## Указать email

```bash
git config --global user.email "you@example.com"
```

Email должен совпадать с email в GitHub, если вы хотите видеть свои коммиты в профиле.

## Последовательность настройки

```bash
git config --global user.name "Ваше Имя"
git config --global user.email "you@example.com"
git config --list
```

Эту последовательность лучше выполнить перед первым коммитом.

---

# 2. Клонирование готового репозитория

## Скачать проект с GitHub на компьютер

```bash
git clone ссылка_на_репозиторий
```

Команда `git clone` скачивает готовый Git-репозиторий на компьютер.

После выполнения команды появится новая папка проекта.

Пример для HTTPS:

```bash
git clone https://github.com/user/repository.git
```

Пример для SSH:

```bash
git clone git@github.com:user/repository.git
```

## Скачать проект в папку с другим именем

```bash
git clone ссылка_на_репозиторий имя_папки
```

Пример:

```bash
git clone git@github.com:user/repository.git my_project
```

В этом случае Git скачает проект не в папку `repository`, а в папку `my_project`.

## Полезные флаги

### `--branch` или `-b`

Флаг `--branch` позволяет сразу скачать конкретную ветку.

```bash
git clone --branch main git@github.com:user/repository.git
```

Короткая запись:

```bash
git clone -b main git@github.com:user/repository.git
```

### `--depth`

Флаг `--depth` позволяет скачать не всю историю коммитов, а только последние коммиты.

```bash
git clone --depth 1 git@github.com:user/repository.git
```

Такой вариант полезен, если проект большой и полная история не нужна.

## Правильная последовательность после clone

```bash
git clone git@github.com:user/repository.git
cd repository
git status
git pull
```

Порядок важен:

1. Сначала скачайте репозиторий через `git clone`.
2. Потом перейдите в папку проекта через `cd`.
3. Потом проверьте состояние через `git status`.
4. Потом можно получить свежие изменения через `git pull`.

После `git clone` не нужно выполнять:

```bash
git init
git remote add origin git@github.com:user/repository.git
```

Команда `git clone` уже сама создает папку `.git` и подключает удаленный репозиторий `origin`.

## Частые ошибки

### Папка уже существует

Если папка с таким именем уже есть, Git может написать:

```text
fatal: destination path 'repository' already exists and is not an empty directory.
```

Что сделать:

1. Выберите другое имя папки.
2. Или перейдите в другую папку.
3. Или удалите старую папку, если она точно не нужна.

Пример с другим именем папки:

```bash
git clone git@github.com:user/repository.git repository_copy
```

### Нет доступа к репозиторию

Если репозиторий приватный или SSH-ключ не настроен, может быть ошибка:

```text
Permission denied
```

или:

```text
Repository not found
```

Что проверить:

1. Есть ли доступ к репозиторию на GitHub.
2. Правильно ли написана ссылка.
3. Настроен ли SSH-ключ, если используется SSH-ссылка.

### Команду запустили внутри другой папки проекта

Так можно случайно скачать один проект внутрь другого проекта.

Перед `git clone` лучше проверить текущую папку:

```bash
pwd
ls
```

На Windows PowerShell:

```powershell
pwd
dir
```

---

# 3. Создание Git-репозитория

## Создать репозиторий в текущей папке

```bash
git init
```

Команда создает скрытую папку `.git`. После этого Git начинает следить за проектом.

## Важная последовательность

```bash
git init
git status
```

Сначала нужно выполнить `git init`, а уже потом `git status`.

Если выполнить `git status` в папке без Git-репозитория, будет ошибка:

```text
fatal: not a git repository
```

---

# 4. Проверка состояния проекта

## Посмотреть состояние файлов

```bash
git status
```

Команда показывает:

1. Какие файлы изменены.
2. Какие файлы добавлены в индекс.
3. Какие файлы еще не отслеживаются Git.
4. Есть ли коммиты, которые нужно отправить на GitHub.

Эту команду полезно выполнять часто.

---

# 5. Добавление файлов в коммит

## Добавить один файл

```bash
git add имя_файла
```

Пример:

```bash
git add main.py
```

## Добавить все изменения

```bash
git add .
```

Точка `.` значит: добавить все изменения из текущей папки и вложенных папок.

## Проверить, что добавилось

```bash
git status
```

## Правильная последовательность

```bash
git status
git add .
git status
```

Сначала лучше посмотреть изменения, потом добавить их, потом снова проверить.

---

# 6. Создание коммита

## Создать коммит

```bash
git commit -m "Короткое описание изменений"
```

Флаг `-m` позволяет сразу написать сообщение коммита.

Пример:

```bash
git commit -m "Добавил инструкцию по Git"
```

## Правильная последовательность

```bash
git status
git add .
git status
git commit -m "Описание изменений"
```

Команду `git commit` нельзя нормально выполнить до `git add`, если изменения еще не добавлены в индекс.

Если выполнить `git commit -m "..."` без `git add`, Git может написать:

```text
nothing added to commit
```

---

# 7. Подключение удаленного репозитория

## Посмотреть удаленные репозитории

```bash
git remote -v
```

Флаг `-v` показывает подробную информацию: имя удаленного репозитория и ссылку.

## Добавить удаленный репозиторий

```bash
git remote add origin ссылка_на_репозиторий
```

Пример для SSH:

```bash
git remote add origin git@github.com:user/repository.git
```

Пример для HTTPS:

```bash
git remote add origin https://github.com/user/repository.git
```

Имя `origin` обычно используют для главного удаленного репозитория.

## Правильная последовательность

```bash
git init
git remote add origin git@github.com:user/repository.git
git remote -v
```

Сначала нужен локальный Git-репозиторий, потом можно добавлять `remote`.

Если выполнить `git remote add ...` не в Git-репозитории, будет ошибка:

```text
fatal: not a git repository
```

---

# 8. Переименование ветки

## Переименовать текущую ветку в `main`

```bash
git branch -M main
```

Флаг `-M` переименовывает текущую ветку принудительно.

Обычно эту команду используют, чтобы главная ветка называлась `main`.

## Правильная последовательность для нового проекта

```bash
git init
git add .
git commit -m "Первый коммит"
git branch -M main
```

Команду `git branch -M main` лучше выполнять после первого коммита.

---

# 9. Отправка изменений на GitHub

## Первый push

```bash
git push -u origin main
```

Флаг `-u` связывает локальную ветку `main` с удаленной веткой `main`.

После этого следующие отправки можно делать короче:

```bash
git push
```

## Правильная последовательность первого push

```bash
git init
git add .
git commit -m "Первый коммит"
git branch -M main
git remote add origin git@github.com:user/repository.git
git push -u origin main
```

Порядок важен:

1. Сначала создается Git-репозиторий.
2. Потом файлы добавляются в коммит.
3. Потом создается коммит.
4. Потом ветка называется `main`.
5. Потом подключается GitHub-репозиторий.
6. Потом изменения отправляются на GitHub.

Если выполнить `git push` до `git commit`, отправлять будет нечего.

Если выполнить `git push` до `git remote add origin ...`, Git не будет знать, куда отправлять изменения.

---

# 10. Получение изменений с GitHub

## Получить изменения

```bash
git pull
```

Команда скачивает изменения из удаленного репозитория и добавляет их в текущую ветку.

## Получить изменения из конкретного remote и ветки

```bash
git pull origin main
```

Здесь `origin` - имя удаленного репозитория, а `main` - имя ветки.

## Правильная последовательность перед началом работы

```bash
git status
git pull
git status
```

Перед `git pull` лучше проверить, нет ли незакоммиченных изменений.

Если у вас есть незакоммиченные изменения, `git pull` может остановиться с ошибкой, чтобы не перезаписать вашу работу.

---

# 11. Обычная последовательность работы каждый день

## Перед началом работы

```bash
git status
git pull
```

Так вы забираете свежие изменения.

## После изменения файлов

```bash
git status
git add .
git status
git commit -m "Описание изменений"
git push
```

Так вы сохраняете изменения в Git и отправляете их на GitHub.

---

# 12. Последовательности, которые нельзя нарушать

## Нельзя делать commit до add

Неправильно:

```bash
git commit -m "Изменения"
git add .
```

Правильно:

```bash
git add .
git commit -m "Изменения"
```

## Нельзя делать push до первого commit

Неправильно:

```bash
git init
git push -u origin main
```

Правильно:

```bash
git init
git add .
git commit -m "Первый коммит"
git push -u origin main
```

## Нельзя делать push без remote

Неправильно:

```bash
git push -u origin main
```

Правильно:

```bash
git remote add origin git@github.com:user/repository.git
git push -u origin main
```

## Нельзя делать pull с незакоммиченными конфликтующими изменениями

Неправильно:

```bash
git pull
```

если перед этим `git status` показывает измененные файлы, которые могут конфликтовать.

Лучше сначала сохранить свои изменения:

```bash
git status
git add .
git commit -m "Сохранил текущие изменения"
git pull
```

## Нельзя делать init после clone

Неправильно:

```bash
git clone git@github.com:user/repository.git
cd repository
git init
```

Правильно:

```bash
git clone git@github.com:user/repository.git
cd repository
git status
```

После `git clone` репозиторий уже создан.

## Нельзя делать remote add origin после clone

Неправильно:

```bash
git clone git@github.com:user/repository.git
cd repository
git remote add origin git@github.com:user/repository.git
```

Правильно:

```bash
git clone git@github.com:user/repository.git
cd repository
git remote -v
```

После `git clone` удаленный репозиторий `origin` уже подключен.

---

# 13. Краткая шпаргалка

## Скачать готовый проект

```bash
git clone git@github.com:user/repository.git
cd repository
git status
```

## Первый запуск Git в проекте

```bash
git init
git status
git add .
git commit -m "Первый коммит"
git branch -M main
git remote add origin git@github.com:user/repository.git
git push -u origin main
```

## Обычная работа

```bash
git pull
git status
git add .
git commit -m "Описание изменений"
git push
```

## Проверки

```bash
git status
git remote -v
git config --list
```
