import pytest

from app.utils.encrypter import Encrypter
from config.config import Config


@pytest.fixture(scope='session')
def encrypter() -> Encrypter:
    cfg: Config = Config.New()

    res: Encrypter = Encrypter.New(cfg)
    return res


@pytest.fixture
def src() -> str:
    return 'secret_password'
