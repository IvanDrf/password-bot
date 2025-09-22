import pytest


from app.repo.repo import Repo
from app.repo.tables import Tables
from tests.repo.fixture import *


@pytest.mark.asyncio
async def test_Add_User(repo: Repo, username: str) -> None:
    await repo.Add_User(username)

    id: int = await repo.Find_User_By_Username(username)
    assert id == 1


@pytest.mark.asyncio
async def test_Bad_Add_User(repo: Repo, username: str) -> None:
    try:
        await repo.Add_User(username)
        pytest.fail(f'shouldnt have added not UNIQUE user in {Tables.users}')
    except Exception as e:
        assert 'UNIQUE' in e.__str__()


@pytest.mark.asyncio
async def test_Find_User(repo: Repo, username: str) -> None:
    user_id: int = await repo.Find_User_By_Username(username)

    assert user_id == 1


@pytest.mark.asyncio
async def test_Bad_Find_User(repo: Repo) -> None:
    try:
        await repo.Find_User_By_Username('')
        pytest.fail(f'shouldnt find user with empty name in {Tables.users}')
    except Exception as e:
        assert e.__str__() == 'cant find user with that username: '


@pytest.mark.asyncio
async def test_Associate_Password(repo: Repo, username: str, password: str, association: str) -> None:
    user_id: int = await repo.Find_User_By_Username(username)

    try:
        await repo.Associate_Password(user_id, password, association)

    except Exception as e:
        assert e.__str__() == ''


@pytest.mark.asyncio
async def test_Bad_Associate_Password(repo: Repo, password: str, association: str) -> None:
    try:
        await repo.Associate_Password(-1, password, association)
        pytest.fail('shouldnt add association with bad user_id')
    except Exception as e:
        assert 'UNIQUE constraint failed' in e.__str__()


@pytest.mark.asyncio
async def test_Find_Password_Associations(repo: Repo, username: str, password: str, association: str) -> None:
    user_id: int = await repo.Find_User_By_Username(username)
    try:
        associations: list[tuple[str, str]] = await repo.Find_Password_Associations(user_id)
        excepted: list[tuple[str, str]] = [(association, password)]

        assert associations == excepted
    except Exception as e:
        pytest.fail(f'shouldnt be a error: {e}')


@pytest.mark.asyncio
async def test_Bad_Find_Password_Associations(repo: Repo) -> None:
    try:
        _: list[tuple[str, str]] = await repo.Find_Password_Associations(-1)
        pytest.fail('should find associations for user who doesnt exist')
    except Exception as e:
        assert e.__str__() == 'cant find associations for this user'


@pytest.mark.asyncio
async def test_Change_Association_Password(repo: Repo, username: str, new_password: str, association: str) -> None:
    user_id: int = await repo.Find_User_By_Username(username)

    try:
        await repo.Change_Association_Password(user_id, new_password, association)

    except Exception as e:
        assert e.__str__() == ''


@pytest.mark.asyncio
async def test_Bad_Change_Association_Password(repo: Repo, username: str, new_password: str, bad_association: str) -> None:
    user_id: int = await repo.Find_User_By_Username(username)
    try:
        await repo.Change_Association_Password(user_id, new_password, bad_association)
        pytest.fail('shouldnt change bad association')
    except Exception as e:
        assert e.__str__() == f'cant find association with {bad_association}'


@pytest.mark.asyncio
async def test_Delete_Association(repo: Repo, username: str, association: str) -> None:
    user_id: int = await repo.Find_User_By_Username(username)

    try:
        await repo.Delete_Association(user_id, association)
    except Exception as e:
        assert e.__str__() == ''


@pytest.mark.asyncio
async def test_Bad_Delete_Association(repo: Repo, username: str, bad_association: str) -> None:
    user_id: int = await repo.Find_User_By_Username(username)

    try:
        await repo.Delete_Association(user_id, bad_association)
        pytest.fail('shouldnt delete bad association')
    except Exception as e:
        assert e.__str__() == f'cant delete association {bad_association}'
