from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message


router = Router()


@router.message(CommandStart())
async def start_function(message: Message):
    await message.answer(f"{message.from_user.username} | {message.from_user.id} Добро пожаловать в наш телеграм бот! Вы можете приобрести премиум-подписку по команде /buy")

