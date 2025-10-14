from typing import TYPE_CHECKING

from app.handlers.registrator.default.default import DefaultRegistrator
from app.handlers.registrator.association.association import AssociationRegistrator
from app.handlers.registrator.message.message import MessageRegistrator
from app.handlers.registrator.password.password import PasswordRegistrator


class Registrator(DefaultRegistrator, PasswordRegistrator, AssociationRegistrator, MessageRegistrator):
    if TYPE_CHECKING:
        from app.handlers.handler import Handler

    def __init__(self, handler: 'Handler') -> None:
        DefaultRegistrator.__init__(self, handler)
        PasswordRegistrator.__init__(self, handler)
        AssociationRegistrator.__init__(self, handler)
        MessageRegistrator.__init__(self, handler)

    def Register_Handlers(self) -> None:
        DefaultRegistrator._Register_Default_Handlers(self)
        PasswordRegistrator._Register_Password_Generation(self)
        AssociationRegistrator._Register_Association(self)
        MessageRegistrator._Register_Messages(self)
