from aiogram.filters import Command
from aiogram.types.bot_command import BotCommand


START_COMMAND = Command("start")
FILM_COMMAND = Command("films")
ADD_FILM_COMMAND = Command("add_film")

COMMANDS = [
    BotCommand(command="start", description="Запуск програми"),
    BotCommand(command="films", description="Показати всі вільми"),
    BotCommand(command="add_film", description="Додати новий фільм")
]
