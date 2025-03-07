from aiogram import Bot, Dispatcher, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import Command, StateFilter

# Укажите токен вашего бота, полученный у BotFather
API_TOKEN = "944480396:AAFAplc2x3vIkTz7Iimq16K03LDzxyowlkE"

# Создаем экземпляры бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Создаем машину состояний
class FSM(StatesGroup):
    converter_state = State()

menu = "/converter - перевод цельсиев в фарингейты\n"

# Хэндлер для команды /start
@dp.message(Command(commands='start'))
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я простой бот на aiogram. Чем могу помочь?")
    await message.answer(f"Вот что я могу:\n{menu}")

# Конвертер температур
@dp.message(Command(commands='converter'))
async def echo_message(message: types.Message, state: FSMContext):
    await message.reply("Вы запустили Конвертацию температуры")
    await message.answer("Введите температуру в Цельсиях")
    # Переключаем состояние на конвертацию
    await state.set_state(FSM.converter_state)

@dp.message(StateFilter(FSM.converter_state))
async def process_cancel_command(message: types.Message, state: FSMContext):
    await message.reply(text=f"Результат: {int(message.text) * 9 / 5 + 32} °F")
    # Отчищаем состояния
    await state.clear()


if __name__ == '__main__':
    print("Запуск бота")
    dp.run_polling(bot)