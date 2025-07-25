from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData


class FilmCallback(CallbackData, prefix="films", sep=";"):
    id: int
    name: str


def films_keyboard_markup(films: list):
    builder = InlineKeyboardBuilder()
    for index, film in enumerate(films):
        callback_data = FilmCallback(id=index, **film)
        builder.button(
            text=callback_data.name,
            callback_data=callback_data.pack()
        )

    builder.adjust(2, repeat=True)
    return builder.as_markup()


def del_film_keyboard(film_id: int):
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Видалити фільм",
        callback_data=f"del_film_{film_id}"
    )
    return builder.as_markup()
