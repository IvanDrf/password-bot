from typing import Final
import aiosqlite

from config.config import Config
from app.repo.query.user.user import UserAdder, UserFinder
from app.repo.query.password.password import PasswordAssociater
from app.repo.query.common.common import Associator

from app.errors.errors import UserException


class Repo:
    def __init__(self, db_name: str) -> None:
        self.__db_name: Final = db_name

    @classmethod
    async def New(cls, cfg: Config) -> 'Repo':
        if cfg.db_name == '':
            raise ValueError('database name is empty in config')

        repo: Repo = cls(cfg.db_name)

        return repo

    async def Add_User(self, username: str) -> None:
        async with aiosqlite.connect(self.__db_name) as db:
            await db.execute(UserAdder.Add_User(), (username,))

            await db.commit()

    async def Find_User_By_Username(self, username: str) -> int | None:
        async with aiosqlite.connect(self.__db_name) as db:
            res = await db.execute_fetchall(UserFinder.Find_UserID_By_Name(), (username,))

            if not res:
                return None

            return list(res)[0][0]

    async def Find_Password_Associations(self, user_id: int) -> list[list[str]]:
        async with aiosqlite.connect(self.__db_name) as db:
            res = await db.execute_fetchall(Associator.Find_User_Passwords(), (user_id,))
            if res is None or not res:
                raise UserException('cant find associations for this user')

            passwords: list[list[str]] = []
            for row in res:
                passwords.append([row[0], row[1]])

            return passwords

    async def Associate_Password(self, user_id: int, password: str, association: str) -> None:
        async with aiosqlite.connect(self.__db_name) as db:
            await db.execute(PasswordAssociater.Associate_Password(),
                             (password, association, user_id))
            await db.commit()

    async def Change_Association_Password(self, user_id: int, password: str, association: str) -> None:
        async with aiosqlite.connect(self.__db_name) as db:
            cursor:  aiosqlite.Cursor = await db.execute(PasswordAssociater.Change_Association_Password(), (password, association, user_id))

            if cursor.rowcount <= 0:
                raise UserException(
                    f'cant find association with {association}')

            await db.commit()

    async def Delete_Association(self, user_id: int, association: str) -> None:
        async with aiosqlite.connect(self.__db_name) as db:
            cursor: aiosqlite.Cursor = await db.execute(PasswordAssociater.Delete_Association(), (user_id, association))
            if cursor.rowcount <= 0:
                raise UserException(
                    f'cant delete association {association}'
                )

            await db.commit()

    async def Delete_All_Associations(self, user_id: int) -> None:
        async with aiosqlite.connect(self.__db_name) as db:
            cursor: aiosqlite.Cursor = await db.execute(PasswordAssociater.Delete_All_Associations(), (user_id,))
            if cursor.rowcount <= 0:
                raise UserException(f'you dont have any associations')

            await db.commit()
