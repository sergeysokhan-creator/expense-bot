import asyncio
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message


TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}!\n"
        "Напиши мне что-нибудь, и я это повторю."
    )


@dp.message(F.text)
async def echo(message: Message):
    await message.answer(f"Ты написал: {message.text}")


async def main():
    if not TOKEN:
        raise RuntimeError("Не задан BOT_TOKEN")
    bot = Bot(token=TOKEN)
    print("Бот запущен. Иди в Telegram и напиши ему.")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
