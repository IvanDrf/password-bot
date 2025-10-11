import pytest


from app.repo.repo import Repo
from app.repo.tables import Tables
from app.errors.errors import UserException
from tests.repo.fixture import *


@pytest.mark.asyncio
async def test_Add_User(repo: Repo, username: str) -> None:
    await repo.Add_User(username)

    id: int | None = await repo.Find_User_By_Username(username)
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
    user_id: int | None = await repo.Find_User_By_Username(username)

    assert user_id == 1


@pytest.mark.asyncio
async def test_Bad_Find_User(repo: Repo) -> None:
    try:
        user_id: int | None = await repo.Find_User_By_Username('')
        assert user_id is None
    except Exception as e:
        pytest.fail('shouldnt raise exception')


@pytest.mark.asyncio
async def test_Associate_Password(repo: Repo, username: str, password: str, association: str) -> None:
    user_id: int | None = await repo.Find_User_By_Username(username)
    if user_id is None:
        pytest.fail('user_id shouldnt be None')

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
    user_id: int | None = await repo.Find_User_By_Username(username)
    if user_id is None:
        pytest.fail('user_id shouldnt be None')

    try:
        associations: list[list[str]] = await repo.Find_Password_Associations(user_id)
        excepted: list[list[str]] = [[association, password]]

        assert associations == excepted
    except Exception as e:
        pytest.fail(f'shouldnt be a error: {e}')


@pytest.mark.asyncio
async def test_Bad_Find_Password_Associations(repo: Repo) -> None:
    try:
        _: list[list[str]] = await repo.Find_Password_Associations(-1)
        pytest.fail('should find associations for user who doesnt exist')
    except Exception as e:
        assert e.__str__() == 'cant find associations for this user'


@pytest.mark.asyncio
async def test_Change_Association_Password(repo: Repo, username: str, new_password: str, association: str) -> None:
    user_id: int | None = await repo.Find_User_By_Username(username)
    if user_id is None:
        pytest.fail('user_id shouldnt be None')
    try:
        await repo.Change_Association_Password(user_id, new_password, association)

    except Exception as e:
        assert e.__str__() == ''


@pytest.mark.asyncio
async def test_Bad_Change_Association_Password(repo: Repo, username: str, new_password: str, bad_association: str) -> None:
    user_id: int | None = await repo.Find_User_By_Username(username)
    if user_id is None:
        pytest.fail('user_id shouldnt be None')

    try:
        await repo.Change_Association_Password(user_id, new_password, bad_association)
        pytest.fail('shouldnt change bad association')
    except Exception as e:
        assert e.__str__() == f'cant find association with {bad_association}'


@pytest.mark.asyncio
async def test_Delete_Association(repo: Repo, username: str, association: str) -> None:
    user_id: int | None = await repo.Find_User_By_Username(username)
    if user_id is None:
        pytest.fail('user_id shouldnt be None')

    try:
        await repo.Delete_Association(user_id, association)
    except Exception as e:
        assert e.__str__() == ''


@pytest.mark.asyncio
async def test_Bad_Delete_Association(repo: Repo, username: str, bad_association: str) -> None:
    user_id: int | None = await repo.Find_User_By_Username(username)
    if user_id is None:
        pytest.fail('user_id shouldnt be None')

    try:
        await repo.Delete_Association(user_id, bad_association)
        pytest.fail('shouldnt delete bad association')
    except Exception as e:
        assert e.__str__() == f'cant delete association {bad_association}'


@pytest.mark.asyncio
async def test_Delete_All_Associations(repo: Repo, username: str, association: str, password: str) -> None:
    user_id: int | None = await repo.Find_User_By_Username(username)
    if user_id is None:
        pytest.fail('user_id shouldnt be None')

    await repo.Associate_Password(user_id, password, association + '1')
    await repo.Associate_Password(user_id, password, association + '2')

    try:
        await repo.Delete_All_Associations(user_id)
    except Exception as e:
        assert e.__str__() == ''

    try:
        await repo.Find_Password_Associations(user_id)
    except UserException as e:
        assert e.__str__() == 'cant find associations for this user'


@pytest.mark.asyncio
async def test_Bad_Delete_All_Associations(repo: Repo, username: str) -> None:
    user_id: int | None = await repo.Find_User_By_Username(username)
    if user_id is None:
        pytest.fail('user_id shouldnt be None')
    try:
        await repo.Delete_All_Associations(user_id)
    except UserException as e:
        assert e.__str__() == 'you dont have any associations'
