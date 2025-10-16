import argparse
import aiosqlite
import asyncio
from typing import Final
from pathlib import Path

from config.config import Config


class Migrator:
    def __init__(self, cfg: Config) -> None:
        self.__db_name: Final = cfg.db_name

        self.__up_migrations_path: Final = cfg.up_migrations_path
        self.__down_migrations_path: Final = cfg.down_migrations_path

    async def Execute_UP_Migrations(self) -> None:
        await self.__Execute_Migrations(self.__up_migrations_path)

    async def Execute_DOWN_Migrations(self) -> None:
        await self.__Execute_Migrations(self.__down_migrations_path)

    async def __Execute_Migrations(self, migrations_path: str) -> None:
        if not Path(migrations_path).exists():
            raise FileExistsError('migrations file is not exists')

        async with aiosqlite.connect(self.__db_name) as db:
            sql_srcipt: str = ''
            with open(migrations_path, 'r') as sql_file:
                sql_srcipt = sql_file.read()

            await db.executescript(sql_srcipt)
            await db.commit()


async def main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument('--migrations')
    args: argparse.Namespace = parser.parse_args()

    migrator: Migrator = Migrator(Config.New())
    task: asyncio.Task

    if args.migrations == 'down':
        task = asyncio.create_task(migrator.Execute_DOWN_Migrations())
    else:
        task = asyncio.create_task(migrator.Execute_UP_Migrations())

    await task

if __name__ == '__main__':
    asyncio.run(main())
