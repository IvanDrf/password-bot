from app.commands.commands import BotCommands

from app.handlers.association.adder import AddHandler
from app.handlers.association.printer import PrintHandler
from app.handlers.association.changer import ChangeHandler
from app.handlers.association.deleter import DeleteHandler


class AssociationHandler(AddHandler, PrintHandler, ChangeHandler, DeleteHandler):
    def __init__(self, commands: BotCommands) -> None:
        AddHandler.__init__(self, commands)
        PrintHandler.__init__(self, commands)
        ChangeHandler.__init__(self, commands)
        DeleteHandler.__init__(self, commands)
