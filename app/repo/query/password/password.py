from app.repo.tables import Tables


class PasswordAssociater:
    @staticmethod
    def Associate_Password() -> str:
        '''password, association, user_id'''
        return f'INSERT INTO {Tables.passwords} (password, association, user_id) VALUES(?, ?, ?)'
