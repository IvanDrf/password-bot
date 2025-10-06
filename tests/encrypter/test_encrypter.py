from utils.encrypter import Encrypter
from tests.encrypter.fixture import encrypter, src


def test_Encryption(encrypter: Encrypter, src: str) -> None:
    encrypted: str = encrypter.encrypt(src.encode()).decode()
    decrypted: str = encrypter.decrypt(encrypted.encode()).decode()

    assert src != encrypted and src == decrypted
