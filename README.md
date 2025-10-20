# 🗺️ Backend_Test_Assignment_PelidTeam

## Описание проекта

Это тестовое задание на вакансию Junior+ backend-разработчика.
Проект представляет собой Django-проект с API для интерактивной карты мест активного отдыха в города, а так же реализацию админ-панели.

Основные технологии:
* **Django** — основной фреймворк backend.
* **FastAPI / ASGI** — для высокопроизводительного API.
* **CKEditor** — WYSIWYG-редактор для админ-панели.
* **SQLite** — база данных по умолчанию.
* **Uvicorn** — ASGI-сервер для запуска проекта.

**API эндпоинты:**
| Метод | URL               | Описание                 |
| ----- | ----------------- | ------------------------ |
| GET   | /api/places/      | Список всех мест         |
| GET   | /api/places/<id>/ | Детали конкретного места |
| GET   | /api/json/        | GeoJSON для карты        |

---

## Установка и настройка

### 1. Клонирование репозитория

```bash
git clone https://github.com/sneJ1k/Backend_Test_Assignment_PelidTeam.git
cd Backend_Test_Assignment_PelidTeam
```

### 2. Создание виртуального окружения

```bash
python3 -m venv .venv
```

### 3. Активация виртуального окружения

* **macOS/Linux:**

```bash
source .venv/bin/activate
```

* **Windows (CMD):**

```cmd
.venv\Scripts\activate
```

* **Windows (PowerShell):**

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Установка зависимостей

```bash
pip install -r requirements.txt
```

---

## Настройка базы данных и фикстур

### 1. Применение миграций

```bash
python manage.py migrate
```

### 2. Загрузка фикстур с начальными данными

Фикстуры создают базовые структуры для отображения функционала API.

```bash
python manage.py loaddata places/fixtures/places.json
```

### 3. Создание суперпользователя

```bash
python manage.py createsuperuser
```

Следуйте инструкциям для ввода имени пользователя, email и пароля.
Суперпользователь нужен для доступа к админ-панели: `http://127.0.0.1:8000/admin/`.

### 4. Собираем статики (для CKEditor и админки) в директорию staticfiles:
```bash
python manage.py collectstatic
```
> Директории media и static включены в репозиторий с заглушками .gitkeep, но по умолчанию пусты. После collectstatic файлы для админки и CKEditor будут скопированы в staticfiles.

---

## Запуск проекта

Проект запускается через **Uvicorn** (ASGI-сервер):

```bash
uvicorn mysite.asgi:app --reload
```

* `--reload` — автоматически перезагружает сервер при изменениях кода.
* Доступ к проекту: `http://127.0.0.1:8000/`
* Админ-панель: `http://127.0.0.1:8000/admin/`

> Все API эндпоинты и админ-панель работают через этот сервер точно так же, как через `manage.py runserver`.

---

## Структура проекта

```
Backend_Test_Assignment_PelidTeam/
├── mysite/                # Основной Django-проект
│   ├── settings.py        # Настройки проекта
│   ├── urls.py            # URL-маршруты
│   ├── asgi.py            # Точка входа ASGI (Uvicorn)
│   └── wsgi.py            # Точка входа WSGI
├── places/                # Приложение для мест
│   ├── fixtures/          # Начальные данные для базы
│   │   └── places.json
│   ├── models.py          # Модели данных
│   ├── api.py             # API для работы с местами интереса
│   ├── apps.py            # Идентификация приложения
│   ├── models.py          # Модели данных
│   ├── tests.py           # Тесты
│   ├── views.py           # Представления и API
│   ├── urls.py            # URL-маршруты
│   └── admin.py           # Настройка админки
├── static/                # Статические файлы (CKEditor, админ-панель)
├── media/                 # Дирректория для хранения медиа-файлов
├── requirements.txt       # Зависимости проекта
└── README.md              # Документация
```

---

## Примечания

* **База данных**: по умолчанию SQLite. Для PostgreSQL или другой СУБД — настройте `settings.py`.
* **Медиа и статика**: `.gitignore` исключает пользовательские файлы и собранную статику.
* **Развертывание**: рекомендуется использовать **Gunicorn**/uWSGI + **Nginx** для продакшн.
