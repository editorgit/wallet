# Wallet API

Django REST API для управления кошельками и транзакциями.

## Описание

Wallet API предоставляет RESTful интерфейс для:
- Создания и управления кошельками
- Выполнения транзакций (пополнение/списание средств)
- Просмотра истории транзакций
- Получения баланса кошельков

## Технический стек

- **Python 3.11**
- **Django 5.2.4**
- **Django REST Framework 3.16.0**
- **PostgreSQL 15**
- **Docker & Docker Compose**
- **Gunicorn** (WSGI сервер)

## Установка и запуск

### Требования

- Docker
- Docker Compose

### Локальная разработка

1. Клонирование репозитория:
```bash
git clone <repository-url>
cd wallet
```

2. Запуск с помощью Docker Compose:
```bash
docker-compose up --build
```

3. API будет доступно по адресу: `http://localhost:8000`

## API Endpoints

API использует JSON:API спецификацию.

### Кошельки

- `GET /api/wallets/` - список всех кошельков
- `POST /api/wallets/` - создание нового кошелька
- `GET /api/wallets/{id}/` - получение кошелька по ID
- `PATCH /api/wallets/{id}/` - обновление кошелька
- `DELETE /api/wallets/{id}/` - удаление кошелька

### Транзакции

- `GET /api/transactions/` - список всех транзакций
- `POST /api/transactions/` - создание новой транзакции
- `GET /api/transactions/{id}/` - получение транзакции по ID
- `GET /api/wallets/{wallet_id}/transactions/` - транзакции конкретного кошелька

## Разработка

### Настройка среды разработки

```bash
# Установка зависимостей
pip install -r requirements.txt

# Применение миграций
python manage.py migrate

# Создание суперпользователя
python manage.py createsuperuser

# Запуск dev сервера
python manage.py runserver
```

### Линтинг и форматирование

Проект использует:
- **Black** для форматирования кода
- **Ruff** для линтинга

```bash
# Форматирование
black .

# Линтинг
ruff check .
```

### Тестирование

```bash
python manage.py test
```
