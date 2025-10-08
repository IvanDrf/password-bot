from app.commands.association.adder import AssociationAdder
from app.commands.association.changer import AssociationChanger
from app.commands.association.deleter import AssociationDeleter
from app.commands.association.printer import AssociationPrinter

from app.repo.repo import Repo

from utils.encrypter import Encrypter


class Associationer(AssociationAdder, AssociationChanger, AssociationDeleter, AssociationPrinter):
    def __init__(self, repo: Repo, encrypter: Encrypter) -> None:
        AssociationAdder.__init__(self, repo, encrypter)
        AssociationChanger.__init__(self, repo, encrypter)
        AssociationDeleter.__init__(self, repo)
        AssociationPrinter.__init__(self, repo, encrypter)
