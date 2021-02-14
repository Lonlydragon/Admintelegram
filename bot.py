
import config
import logging
import price

from aiogram import Bot, Dispatcher, executor, types

# задаем уровень логов
logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TELEGRAM_API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(content_types=["new_chat_members"])
async def send_welcome(message: types.message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    user_name = message.from_user.first_name
    await message.chat.promote(user_id=message.from_user.id, can_delete_messages=False, can_pin_messages=True,
                                   can_invite_users=True, can_change_info=True)
    await message.answer("{} выданы админские права, Lalka".format(user_name))
    await message.chat.set_administrator_custom_title(user_id=message.from_user.id, custom_title="Lalka")

@dp.message_handler(content_types=["left_chat_member"])
async def send_welcome(message: types.message):
    user_name = message.from_user.first_name
    await message.answer("{} прощай, Lalka".format(user_name))

@dp.message_handler(commands=['usdrub'])
async def curse(message: types.message):
    usd_rub = price.get_usd_course()
    await message.answer("Курс доллара: {}".format(usd_rub))

@dp.message_handler(commands=['tesla'])
async def curse(message: types.message):
    tsla = price.get_tsla_price()
    await message.answer("Курс акциий Tesla: {}".format(tsla))

@dp.message_handler(commands=['apple'])
async def curse(message: types.message):
    apple = price.get_apple_price()
    await message.answer("Курс акций Apple: {}".format(apple))

@dp.message_handler(lambda message: message.text and 'дай права' in message.text.lower())
async def send_welcome(message: types.message):
    await message.chat.promote(user_id=message.from_user.id, can_delete_messages=False, can_pin_messages=True,
                                   can_invite_users=True, can_change_info=True)
    await message.answer("{} выданы админские права, Lalka".format(message.from_user.first_name))
    await message.chat.set_administrator_custom_title(user_id=message.from_user.id, custom_title="Lalka")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
