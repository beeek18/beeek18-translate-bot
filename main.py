import asyncio
import logging
import os
from pathlib import Path

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from bot.handlers import router

load_dotenv()


def setup_logging() -> None:
    """Настройка логирования: одновременно в файл и в консоль."""
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)

    log_format = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
    date_format = "%d-%m-%Y %H:%M:%S"

    logging.basicConfig(
        level=logging.INFO,
        format=log_format,
        datefmt=date_format,
        handlers=[
            # В файл
            logging.FileHandler("logs/bot.log", encoding="utf-8"),
            # В консоль
            logging.StreamHandler(),
        ],
    )


async def main() -> None:
    setup_logging()
    logger = logging.getLogger(__name__)

    token = os.getenv("BOT_TOKEN")
    if not token:
        raise ValueError("BOT_TOKEN не найден. Проверь .env файл.")

    bot = Bot(token=token)
    dp = Dispatcher()
    dp.include_router(router)

    logger.info("Бот запускается...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
