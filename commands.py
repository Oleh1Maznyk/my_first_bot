from aiogram.filters import Command
from aiogram.types.bot_command import BotCommand


START_COMMAND = Command("start")
FILM_COMMAND = Command("films")
ADD_FILM_COMMAND = Command("add_film")
SEARCH_BY_ACTOR = Command("search_by_actor")
DELETE_FILM = Command("delete_film")

COMMANDS = [
    BotCommand(command="start", description="Запуск програми"),
    BotCommand(command="films", description="Показати всі фільми"),
    BotCommand(command="add_film", description="Додати новий фільм"),
    BotCommand(command="search_by_actor", description="Знайти фільм за імям автора"),
    BotCommand(command="delete_film", description="Видалити фільм")
]
