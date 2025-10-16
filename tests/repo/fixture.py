import pytest
import pytest_asyncio
from typing import Final

from app.repo.repo import Repo
from config.config import Config
from migrations.migrator import Migrator

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
    cfg: Config = Config(token='', db_name=db_name, up_migrations_path='migrations/1_create_tables.up.sql',
                         down_migrations_path='migrations/1_drop_tables.down.sql', key='', logger_level='')

    repo: Repo = await Repo.New(cfg)

    migrator: Migrator = Migrator(cfg)
    await migrator.Execute_DOWN_Migrations()
    await migrator.Execute_UP_Migrations()

    return repo
