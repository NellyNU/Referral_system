# Referral System

## Installation and Setup

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up the PostgreSQL database
4. Create migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Start the server:
   ```
   python manage.py runserver
   ```

## API Endpoints

### Phone Authorization

1. **Send Code**
   - URL: `/api/users/auth/phone/`
   - Method: POST
   - Parameters: `phone_number`

2. **Verify Code**
   - URL: `/api/users/auth/verify/`
   - Method: POST
   - Parameters: `phone_number`, `code`

### User Profile

1. **Get Profile**
   - URL: `/api/users/profile/`
   - Method: GET
   - Authorization Required

## API Documentation

Swagger: `/swagger/`  
ReDoc: `/redoc/`



# Система Рефералов

## Установка и запуск

1. Клонируйте репозиторий
2. Установите зависимости:
   ```
   pip install -r requirements.txt
   ```

3. Настройте базу данных PostgreSQL
4. Создайте миграции:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Запустите сервер:
   ```
   python manage.py runserver
   ```

## API Эндпоинты

### Авторизация по телефону

1. **Отправка кода**
   - URL: `/api/users/auth/phone/`
   - Метод: POST
   - Параметры: `phone_number`

2. **Верификация кода**
   - URL: `/api/users/auth/verify/`
   - Метод: POST
   - Параметры: `phone_number`, `code`

### Профиль пользователя

1. **Получение профиля**
   - URL: `/api/users/profile/`
   - Метод: GET
   - Требуется авторизация

## Документация API

Swagger: `/swagger/`
ReDoc: `/redoc/`
