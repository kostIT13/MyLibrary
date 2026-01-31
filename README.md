# 📚 MyLibrary FastAPI - Библиотечная система

Современная система управления библиотекой на FastAPI с полным CRUD функционалом.

# 🚀 Быстрый старт

1. Клонировать репозиторий

git clone https://github.com/kostIT13/MyLibrary.git

cd MyLibrary

2. Создать виртуальное окружение

python -m venv venv

venv\Scripts\activate  # Windows

source venv/bin/activate  # Linux/Mac

3. Установить зависимости

pip install -r requirements.txt

4. Запустить сервер

uvicorn main:app --reload

# 🌐 Доступные адреса

Swagger UI документация: http://localhost:8000/docs

ReDoc документация: http://localhost:8000/redoc

# 📖 API Endpoints

Метод	Endpoint	Описание

GET	/books/	Список книг с пагинацией

GET	/books/{id}	Книга по ID

POST	/books/	Добавить книгу

PUT	/books/{id}	Обновить книгу

DELETE	/books/{id}	Удалить книгу

# 🏗️ Структура проекта

text
```
MyLibrary/
├── main.py              # Точка входа FastAPI
├── database.py          # Подключение к БД
├── repository.py        # Работа с данными
├── requirements.txt     # Зависимости
├── models/book.py       # SQLAlchemy модели
├── schemas/book.py      # Pydantic схемы
└── routers/books.py     # Маршруты API
```

# 🛠️ Технологии

FastAPI — веб-фреймворк для API

SQLAlchemy — ORM для работы с БД

Pydantic — валидация данных

Uvicorn — ASGI-сервер

SQLite — база данных

