from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '2035083847:AAG_Yt90Bdl-ZgNhfHlKg5p0JN32_H8Iav4'

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):
    print(message)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)