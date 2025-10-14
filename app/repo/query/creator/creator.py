from typing import Final
from app.repo.tables import Tables


class TableCreator:
    __user_table: Final = f'''
CREATE TABLE IF NOT EXISTS {Tables.users}(
    user_id INTEGER PRIMARY KEY,
    username TEXT UNIQUE
)
'''

    __passwords_table: Final = f'''
CREATE TABLE IF NOT EXISTS {Tables.passwords}(
    password TEXT NOT NULL,
    association TEXT NOT NULL UNIQUE,
    user_id INTEGER,

    FOREIGN KEY (user_id) REFERENCES {Tables.users}(user_id)
)
'''

    @staticmethod
    def Create_Users_Table() -> str:
        return TableCreator.__user_table

    @staticmethod
    def Create_Passwords_Talbe() -> str:
        return TableCreator.__passwords_table
