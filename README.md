## Подготовка

- Установить проект;
- Создать и активировать виртуальное окружение python -m venv venv;
- Установить зависимости pip install -r requirements.txt;
- Изменить данные для подключения к БД "PostgreSQL" в файле "env";
- Установить фикстуры в БД "PostgreSQL" из папки "fixtures" находящийся в "users";
- Установите играции командой: "python manage.py migrate".
- Запусть файл "csu.py" для создания суперпользователя командой: "python manage.py csu".
- Запусть файл проект командой: "python manage.py runserver".
