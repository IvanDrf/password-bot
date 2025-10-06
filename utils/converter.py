class NumberConverter:
    @staticmethod
    def From_Str_To_Positive_Int(src: str) -> int:
        try:
            number: int = int(src)
        except:
            raise ValueError('given not a number')

        if number <= 0:
            raise ValueError('given not positive number')

        return number


class MessageParser:
    @staticmethod
    def ParseMessage(src: str) -> tuple[str, str]:
        '''parse message from 'a b' -> [a, b] '''
        association: str = ''
        password: str = ''

        try:
            association, password = src.split()
        except:
            raise ValueError('format should be name password')

        return association, password
