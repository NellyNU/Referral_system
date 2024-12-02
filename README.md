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
