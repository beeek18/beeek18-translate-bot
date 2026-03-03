import logging
from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from bot.transliterate import transliterate, is_cyrillic_fio

router = Router()
logger = logging.getLogger(__name__)


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    if message.from_user is None:
        return
    logger.info(
        f"User {message.from_user.id} ({message.from_user.username}) started the bot"
    )
    await message.answer(
        "👋 Привет! Я бот для транслитерации ФИО.\n\n"
        "Отправь мне ФИО на <b>кириллице</b> — я переведу его на латиницу "
        "по <b>Приказу МИД России № 2113 от 12.02.2020</b>.\n\n"
        "Пример:\n"
        "➡️ <i>Иванов Иван Иванович</i>\n"
        "✅ <b>Ivanov Ivan Ivanovich</b>",
        parse_mode="HTML",
    )


@router.message(Command("help"))
async def cmd_help(message: Message) -> None:
    if message.from_user is None:
        return
    logger.info(f"User {message.from_user.id} requested help")
    await message.answer(
        "📖 <b>Как пользоваться:</b>\n\n"
        "Просто напиши ФИО на кириллице — и получишь транслитерацию.\n\n"
        "Допустимые символы: буквы кириллицы, пробелы, дефис.\n\n"
        "Команды:\n"
        "/start — начало работы\n"
        "/help — эта справка",
        parse_mode="HTML",
    )


@router.message()
async def handle_fio(message: Message) -> None:
    if message.from_user is None or message.text is None:
        return
    text = message.text.strip()
    user_id = message.from_user.id
    username = message.from_user.username

    logger.info(f"User {user_id} ({username}) sent: {text!r}")

    if not is_cyrillic_fio(text):
        logger.warning(f"User {user_id} sent invalid input: {text!r}")
        await message.answer(
            "⚠️ Пожалуйста, введи ФИО <b>только на кириллице</b>.\n"
            "Допустимы буквы, пробелы и дефис.\n\n"
            "Пример: <i>Петров-Водкин Кузьма Сергеевич</i>",
            parse_mode="HTML",
        )
        return

    result = transliterate(text)
    logger.info(f"User {user_id} result: {result!r}")

    await message.answer(f"<code>{result}</code>", parse_mode="HTML")
