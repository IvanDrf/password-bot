import aiosqlite
import pytest_asyncio
import pytest

from typing import Final

from app.repo.repo import Repo
from app.repo.tables import Tables
from config.config import Config

db_name: Final = 'test.db'


@pytest.fixture
def user() -> str:
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


@pytest_asyncio.fixture(scope='session')
async def repo() -> Repo:
    cfg: Config = Config(token='', db_name=db_name)

    await Drop_Tables()
    repo: Repo = await Repo.New(cfg)

    return repo


@pytest.mark.asyncio
async def test_Add_User(repo: Repo, user: str) -> None:
    await repo.Add_User(user)

    id: int = await repo.Find_User_By_Username(user)
    assert id == 1


@pytest.mark.asyncio
async def test_Bad_Add_User(repo: Repo, user: str) -> None:
    try:
        await repo.Add_User(user)
        pytest.fail(f'shouldnt have added not UNIQUE user in {Tables.users}')
    except Exception as e:
        assert 'UNIQUE' in e.__str__()


@pytest.mark.asyncio
async def test_Find_User(repo: Repo, user: str) -> None:
    user_id: int = await repo.Find_User_By_Username(user)

    assert user_id == 1


@pytest.mark.asyncio
async def test_Bad_Find_User(repo: Repo) -> None:
    try:
        await repo.Find_User_By_Username('')
        pytest.fail(f'shouldnt find user with empty name in {Tables.users}')
    except Exception as e:
        assert e.__str__() == 'cant find user with that username: '


@pytest.mark.asyncio
async def test_Associate_Password(repo: Repo, user: str, password: str, association: str) -> None:
    user_id: int = await repo.Find_User_By_Username(user)

    try:
        await repo.Associate_Password(user_id, password, association)

    except Exception as e:
        assert e.__str__() == ''


@pytest.mark.asyncio
async def test_Change_Association_Password(repo: Repo, user: str, new_password: str, association: str) -> None:
    user_id: int = await repo.Find_User_By_Username(user)

    try:
        await repo.Change_Association_Password(user_id, new_password, association)

    except Exception as e:
        assert e.__str__() == ''


async def Drop_Tables() -> None:
    async with aiosqlite.connect(db_name) as db:
        await db.execute(f'DROP TABLE IF EXISTS {Tables.passwords}')
        await db.execute(f'DROP TABLE IF EXISTS {Tables.users}')

        await db.commit()
