from aiogram import *
import config

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f'Здравствуйте, {message.from_user.first_name}! \nЕсли вы хотите поделиться своим предложением, то просто пришлите в этот чат свои фото / видео / текст')


@dp.message_handler(content_types=['text', 'voice', 'document', 'photo', 'sticker', 'video', 'video_note',
                                   'poll'])  # в chat_id указать id админа
async def offer(message: types.Message):
    await bot.send_message(message.from_user.id, 'Ваше предложение отправлено!')
    await bot.forward_message(chat_id=414257117, from_chat_id=message.from_user.id, message_id=message.message_id)


executor.start_polling(dp, skip_updates=True)
