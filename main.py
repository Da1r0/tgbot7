import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from callback.shop import ShopCallback
from keyboards.menu import main_menu_command

from config import config
from keyboards.inline import shop_keyboards

API_TOKEN = config.token

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
@dp.message(Command(commands='start'))
async def start_command(message: Message):
    await message.answer('Привет')
@dp.message(Command(commands='shop'))
async def shop_command(message: Message):
    await message.answer('В нашем магазине есть следующие товары:', reply_markup=shop_keyboards)

@dp.callback_query(ShopCallback.filter())
async def handle_cats(query: CallbackQuery, callback_data: ShopCallback):
    await query.answer(f'Покупка совершена')
    await query.message.answer(f'Товар: {callback_data.shop}. Количество: {callback_data.count}')


async def main():
    try:
        print('Bot Started')
        await bot.set_my_commands(main_menu_command)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':  # Если мы запускаем конкретно этот файл.
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')

