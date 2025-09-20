from app.repo.tables import Tables


class Associator:
    @staticmethod
    def Find_User_Passwords() -> str:
        '''want: user_id'''
        return f'SELECT association, password FROM {Tables.passwords} WHERE user_id = ?'
