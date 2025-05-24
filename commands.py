from aiogram.filters import Command
from aiogram.types.bot_command import BotCommand


FILM_COMMAND = Command("films")
START_COMMAND = Command("start")

COMMANDS = [
    BotCommand(command="films", description="Показати всі вільми"),
    BotCommand(command="start", description="Запуск програми")
]
