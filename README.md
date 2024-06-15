# Mirea API

![Python](https://img.shields.io/badge/Python-3.x-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.73.0-green)

## Обзор
Mirea API — это RESTful сервис, созданный с использованием FastAPI для получения ответов на тесты/вопросы. Этот API предоставляет возможность получить ответ от ChatGPT без использования VPN. Данный API используется для моего расширения [MIREA Extension](https://github.com/Juonior/mirea_extension)

## Особенности
- **FastAPI**: Высокая производительность, легкость в изучении, быстрая разработка, готовность к продакшену.
- **Модульная структура**: Организация в модули для лучшей масштабируемости и поддержки.
- **Конфигурация окружения**: Легко настраивается с помощью переменных окружения.

## Установка

1. **Клонируйте репозиторий:**
    ```sh
    git clone https://github.com/Juonior/mirea_api.git
    cd mirea_api
    ```

2. **Создайте и активируйте виртуальное окружение:**
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Установите зависимости:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Настройте переменные окружения:**
    Скопируйте `.env.example` в `.env` и настройте необходимые переменные.

## Использование

Чтобы запустить сервер, выполните:
```sh
python3 main.py
```

API будет доступен по адресу `http://localhost:8000`.

## Структура проекта

```
mirea_api/
│
├── core/
│   └── config.py
├── routers/
│   └── getAnswer.py
├── services/
│   └── openai_service.py
├── .env.example
├── .gitignore
├── main.py
└── requirements.txt
```

- **core**: Содержит файлы конфигурации.
- **routers**: Содержит определения маршрутов для различных модулей.
- **services**: Содержит логику для обработки данных.

