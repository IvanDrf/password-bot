from app.repo.tables import Tables


class UserAdder:
    @staticmethod
    def Add_User() -> str:
        '''username'''
        return f'INSERT INTO {Tables.users} (username) VALUES(?)'


class UserFinder:
    @staticmethod
    def Find_UserID_By_Name() -> str:
        '''username'''
        return f'SELECT user_id FROM {Tables.users} WHERE username = ?'
