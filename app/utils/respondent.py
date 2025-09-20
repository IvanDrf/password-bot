class Respondent:
    @staticmethod
    def Create_Associations_List(associations: list[tuple[str, str]]) -> str:
        return '\n'.join(
            f'{i+1}) {association} | {password}' for i, (association, password) in enumerate(associations)
        )
