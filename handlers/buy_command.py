from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from ansar_aiogram_bot_8.utils.constants import PRICES
from ansar_aiogram_bot_8.config.settings import PAYMENT_TOKEN

router = Router()


@router.message(Command('buy'))
async def buy_function(message: Message):
    await message.bot.send_invoice(
        chat_id=message.from_user.id,
        title="Премиум Подписка",
        description="Доступ к эксклюзивным данным",
        payload="premium-access",
        provider_token=PAYMENT_TOKEN,
        currency="RUB",
        prices=PRICES
    )
