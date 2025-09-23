import pytest
import pytest_asyncio
import aiosqlite
from typing import Final

from app.repo.repo import Repo
from app.repo.tables import Tables
from app.utils.encrypter import Encrypter
from config.config import Config

db_name: Final = 'test.db'


@pytest.fixture
def username() -> str:
    return 'test_user'


@pytest.fixture
def password() -> str:
    return 'super_password'


@pytest.fixture
def new_password() -> str:
    return 'new_super_password'


@pytest.fixture
def association() -> str:
    return 'association_example'


@pytest.fixture
def bad_association() -> str:
    return 'bad_association'


@pytest_asyncio.fixture(scope='session')
async def repo() -> Repo:
    cfg: Config = Config(token='', db_name=db_name, key='')

    await Drop_Tables()
    repo: Repo = await Repo.New(cfg)

    return repo


async def Drop_Tables() -> None:
    async with aiosqlite.connect(db_name) as db:
        await db.execute(f'DROP TABLE IF EXISTS {Tables.passwords}')
        await db.execute(f'DROP TABLE IF EXISTS {Tables.users}')

        await db.commit()
