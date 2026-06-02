from aiogram import Router


router = Router()

from ansar_aiogram_bot_8.handlers.start_command import router as start_command_router
router.include_router(start_command_router)
from ansar_aiogram_bot_8.handlers.buy_command import router as buy_command_router
router.include_router(buy_command_router)