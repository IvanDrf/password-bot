from aiogram import Dispatcher, F
from aiogram.filters import CommandStart, Command


class Handler:
    dp: Dispatcher = Dispatcher()

    @staticmethod
    def Register_Handlers() -> None:
        from .commands import Start_Handler, Help_Handler
        from .messages import Message_Handler

        Handler.dp.message.register(Start_Handler, CommandStart())
        Handler.dp.message.register(Help_Handler, Command('help'))

        Handler.dp.message.register(Message_Handler, F.text)
