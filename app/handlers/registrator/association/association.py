from typing import TYPE_CHECKING

from app.handlers.registrator.association.adder import AdderRegistrator
from app.handlers.registrator.association.changer import ChangerRegistrator
from app.handlers.registrator.association.deleter import DeleterRegistrator
from app.handlers.registrator.association.printer import PrinterRegistrator


class AssociationRegistrator(AdderRegistrator, ChangerRegistrator, DeleterRegistrator, PrinterRegistrator):
    if TYPE_CHECKING:
        from app.handlers.handler import Handler

    def __init__(self, handler: 'Handler') -> None:
        AdderRegistrator.__init__(self, handler)
        ChangerRegistrator.__init__(self, handler)
        DeleterRegistrator.__init__(self, handler)
        PrinterRegistrator.__init__(self, handler)

    def _Register_Association(self) -> None:
        AdderRegistrator._Register_Password_Association(self)
        ChangerRegistrator._Register_Association_Changing(self)
        DeleterRegistrator._Register_Deletion(self)
        PrinterRegistrator._Register_Association_Print(self)
