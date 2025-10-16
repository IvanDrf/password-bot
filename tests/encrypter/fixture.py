import pytest
from typing import Final

from utils.encrypter import Encrypter
from config.config import Config

random_key: Final = 'u5HjK9n2XcQ7vEa1lP8gYmZpOqBwRkDyS3TfWxN0LtM='


@pytest.fixture(scope='session')
def encrypter() -> Encrypter:
    cfg: Config = Config(token='', db_name='', up_migrations_path='', down_migrations_path='',
                         key=random_key, logger_level='')

    res: Encrypter = Encrypter.New(cfg)
    return res


@pytest.fixture
def src() -> str:
    return 'secret_password'
