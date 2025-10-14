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
