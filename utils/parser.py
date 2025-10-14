class MessageParser:
    @staticmethod
    def ParseMessage(src: str) -> tuple[str, str]:
        '''parse message from 'a b' -> [a, b] '''
        association: str = ''
        password: str = ''

        try:
            association, password = src.split()
        except:
            raise ValueError('format should be "first" "second"')

        return association, password
