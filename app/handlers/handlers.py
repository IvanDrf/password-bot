from aiogram import Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State


class Handler:
    dp: Dispatcher = Dispatcher()

    @staticmethod
    def Register_Handlers() -> None:
        from .commands import Start_Handler, Help_Handler, Generate_Handler, Input_Length
        from .messages import Message_Handler

        Handler.dp.message.register(Start_Handler, CommandStart())
        Handler.dp.message.register(Help_Handler, Command('help'))
        Handler.dp.message.register(Generate_Handler, Command('generate'))
        Handler.dp.message.register(Input_Length,  State)

        Handler.dp.message.register(Message_Handler, F.text)
