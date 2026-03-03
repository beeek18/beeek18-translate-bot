# 🤖 Translate Bot — транслитерация ФИО по Приказу МИД № 2113

Телеграм-бот, который принимает ФИО на кириллице и возвращает транслитерацию на латиницу в соответствии с [Приказом МИД России от 12.02.2020 № 2113](https://www.consultant.ru/document/cons_doc_LAW_360580/).

## 🚀 Запуск через Docker

### 1. Клонируй репозиторий

```bash
git clone https://github.com/beeek18/beeek18_translate_bot.git
cd beeek18_translate_bot
```

### 2. Создай `.env` файл

```bash
cp .env.example .env
```

Открой `.env` и вставь токен своего бота:

```env
BOT_TOKEN=your_telegram_bot_token_here
```

### 3. Запусти через Docker Compose

```bash
docker compose up --build -d
```

Бот запустится в фоне. Логи будут сохраняться в папку `./logs/bot.log`.

### 4. Просмотр логов

```bash
# Логи контейнера (консоль)
docker compose logs -f

# Логи из файла
cat logs/bot.log
```

### 5. Остановка

```bash
docker compose down
```

---

## 💻 Запуск локально (без Docker)

```bash
# Создать окружение и установить зависимости
uv sync

# Запустить
uv run main.py
```

---

## 📋 Таблица транслитерации

Реализована полная таблица по Приказу МИД № 2113:

| Кириллица | Латиница |
|-----------|----------|
| а | a |
| б | b |
| в | v |
| г | g |
| д | d |
| е, ё | e |
| ж | zh |
| з | z |
| и, й | i |
| к | k |
| л | l |
| м | m |
| н | n |
| о | o |
| п | p |
| р | r |
| с | s |
| т | t |
| у | u |
| ф | f |
| х | kh |
| ц | ts |
| ч | ch |
| ш | sh |
| щ | shch |
| ъ | ie |
| ы | y |
| ь | (не отображается) |
| э | e |
| ю | iu |
| я | ia |

---

## 🗂 Структура проекта

```
beeek18_translate_bot/
├── bot/
│   ├── __init__.py
│   ├── handlers.py       # обработчики сообщений
│   └── transliterate.py  # логика транслитерации
├── logs/                 # логи (создаётся автоматически)
├── main.py               # точка входа
├── .env                  # токен (не коммитится)
├── .env.example          # шаблон
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```
---

## 🐍 Требования

- Python 3.13+
- Docker & Docker Compose
- uv (для локального запуска)