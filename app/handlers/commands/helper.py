from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from typing import Final


class Helper:
    help_command: Final = '''
Commands:
/start - start bot
/help - display the list of available commands
/generate - start generating a new password
/associate - associate word with your password
/change - change password to your association
/del - delete your association
/my - print your associations
'''

    def __init__(self) -> None:
        pass

    async def Help(self, message: Message, state: FSMContext) -> None:
        await state.clear()

        await message.answer(Helper.help_command)
