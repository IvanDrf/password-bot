from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.repo.repo import Repo
from app.state.state import AssociationStates
from app.errors.errors import UserException


class AssociationDeleter:
    def __init__(self, repo: Repo) -> None:
        self.repo: Repo = repo

    async def Start_Association_Deletion(self, message: Message, state: FSMContext) -> None:
        await state.clear()

        await message.answer('Enter the association you want to delete, for example: github')
        await state.set_state(AssociationStates.waiting_deletion_association)

    async def Delete_Association(self, message: Message, state: FSMContext) -> None:
        if message.from_user is None or message.from_user.username is None:
            await message.answer('Cant find your username')
            return

        try:
            if message.text is None:
                raise ValueError('message is empty')

            user_id: int = await self.repo.Find_User_By_Username(message.from_user.username)

            await self.repo.Delete_Association(user_id, message.text)

            await message.answer(f'Successfully deleted your association {message.text}')
            await state.clear()
        except ValueError as e:
            await message.answer(f'Invalid input, error: {e}')

        except UserException as e:
            await message.answer(f'Error: {e}')

        except Exception as e:
            await message.answer(f'Cant find your association {message.text}')

    async def Start_All_Associations_Deletion(self, message: Message, state: FSMContext) -> None:
        await state.clear()

        await message.answer('Are you sure, you want to delete ALL your associations(y/n)?')
        await state.set_state(AssociationStates.waiting_deletion_all_associations)

    async def Delete_All_Associations(self, message: Message, state: FSMContext) -> None:
        if message.from_user is None or message.from_user.username is None:
            await message.answer('Cant find your username')
            return

        try:
            if message.text is None:
                raise ValueError('message is empty')

            if message.text == 'y':
                user_id: int = await self.repo.Find_User_By_Username(message.from_user.username)
                await self.repo.Delete_All_Associations(user_id)

                await message.answer('Successfully deleted all your associations')
            else:
                await message.answer('Everything is okay with your associations')

            await state.clear()

        except Exception as e:
            await message.answer(f'Error: {e}')
