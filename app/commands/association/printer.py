from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.repo.repo import Repo
from utils.encrypter import Encrypter
from utils.respondent import Respondent


class AssociationPrinter:
    def __init__(self, repo: Repo, encrypter: Encrypter) -> None:
        self.repo: Repo = repo
        self.encrypter: Encrypter = encrypter

    async def Print_User_Associations(self, message: Message, state: FSMContext) -> None:
        await state.clear()

        if message.from_user is None or message.from_user.username is None:
            await message.answer('Cant find your username')
            return

        try:
            user_id: int | None = await self.repo.Find_User_By_Username(message.from_user.username)
            if user_id is None:
                await message.answer(f'Cant find you in database, please enter /start')
                return

            associations: list[list[str]] = await self.repo.Find_Password_Associations(user_id)

            for i in range(len(associations)):
                associations[i][1] = self.encrypter.decrypt(
                    associations[i][1]).decode()

            answer: str = Respondent.Create_Associations_List(
                associations)

            await message.answer(answer)
        except:
            await message.answer('You dont have any associations')
