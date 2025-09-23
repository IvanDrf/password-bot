import pytest
from typing import Final

from app.utils.encrypter import Encrypter
from config.config import Config

random_key: Final = 'u5HjK9n2XcQ7vEa1lP8gYmZpOqBwRkDyS3TfWxN0LtM='


@pytest.fixture(scope='session')
def encrypter() -> Encrypter:
    cfg: Config = Config(token='', db_name='',
                         key=random_key)

    res: Encrypter = Encrypter.New(cfg)
    return res


@pytest.fixture
def src() -> str:
    return 'secret_password'
