from aiogram.filters.callback_data import CallbackData
class ShopCallback(CallbackData, prefix='shop'):
    shop: str
    count: int