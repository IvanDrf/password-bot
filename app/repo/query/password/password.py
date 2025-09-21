from app.repo.tables import Tables


class PasswordAssociater:
    @staticmethod
    def Associate_Password() -> str:
        '''want: password, association, user_id'''
        return f'INSERT INTO {Tables.passwords} (password, association, user_id) VALUES(?, ?, ?)'

    @staticmethod
    def Change_Association_Password() -> str:
        '''want: password, association, user_id'''
        return f'UPDATE {Tables.passwords} SET password = ? WHERE association = ? AND user_id = ?'
