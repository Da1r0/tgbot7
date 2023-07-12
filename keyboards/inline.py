from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from callback.shop import ShopCallback

soup = InlineKeyboardButton(text='Мыло', callback_data=ShopCallback(shop='Мыло', count=4).pack())
shampoo = InlineKeyboardButton(text='Шампунь', callback_data=ShopCallback(shop='Шампунь', count=3).pack())
gel = InlineKeyboardButton(text='Гель', callback_data=ShopCallback(shop='Гель', count=2).pack())
cream = InlineKeyboardButton(text='Крем', callback_data=ShopCallback(shop='Крем', count=1).pack())

shop_keyboards = InlineKeyboardMarkup(inline_keyboard=[
    [soup, shampoo],
    [gel, cream]

])
ShopCallback(shop='Мыло', count=4).pack()
ShopCallback(shop='Шампунь', count=3).pack()
ShopCallback(shop='Гель', count=2).pack()
ShopCallback(shop='Крем', count=1).pack()