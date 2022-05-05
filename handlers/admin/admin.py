from aiogram import types
from aiogram.dispatcher.filters import Command

from config import CHAT_ID
from loader import dp, db
from utils.throttlig import rate_limit


@rate_limit(limit=3)
@dp.message_handler(Command('rating_book'))
async def rating(message: types.Message):

    count = await db.select_count_values('books')
    return await message.answer(text=f'Всего было скачано книг: {count}')


@rate_limit(limit=3)
@dp.message_handler(Command('rating_user'))
async def rating(message: types.Message):

    count = await db.select_count_values('users')
    return await message.answer(text=f'Всего в базе пользователей: {count}')


@dp.message_handler(Command('delete'))
async def delete_table(message: types.Message):
    args = message.get_args()
    if args == 'tables' and message.from_user.id == CHAT_ID:
        await db.delete_table_pages()
        await db.create_tables()
    return await message.answer('Таблицы были удалены!')


@dp.message_handler(content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def check_new_user(message: types.Message):
    '''
    Проверка нового юзера вступившего в группу, чтобы не было ботов в группе
    '''
    new_user = message.new_chat_members[0]

    if new_user.is_bot:
        return await dp.bot.kick_chat_member(message.chat.id, new_user.id)
