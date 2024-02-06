from dataclasses import dataclass

"""Ce fichier montre des exemples d'erreurs de linting"""

MA_VARIABLE = 1


class MaClass:
    def __init__(self):
        self.ma_variable = 1


mon_caractère = (
    "C'est une très longue ligne ce n'est pas une bonne façon d'écrire du code python"  # noqa: E501
    + "vous voulez évitez des erreurs de linting que va detecter pylint comme c030"  # noqa: E501
)


mon_caractère = "Bonjour, Toi!   "

ma_variable = 1


def ma_fonction():
    print("Bonjour, toi")

    if True:
        print("Bonjour, toi!")
        print("Bonjour, toi!")


def ma_fonction(ma_variable):
    print(ma_variable)


ma_fonction()

ma_variable = 45


def ma_fonction(ma_variable):
    print(ma_variable)


ma_fonction(ma_variable=1, ma_seconde_variable=2)


from dataclasses import dataclass


@dataclass
class Livre:
    title: str
    nombre_pages: int
    author: str
    genre: str
    poids: int
    prix: float
    dispo: str
    bbb: str
    kopp: str
    manufacturer: str
    pays: str
    resumer: str
    kkx: str
    ppc: int
    categorie: str
    aadf: int
    mdfk: int
    akadio: float
    mma: int


def somme_nombres(a: float, b: float) -> float:
    """
    Retourne la somme de e et b.

    Args:
        a (int): premier argument
        b (float): deuxième argument

    Returns:
        float: la somme de a et b

    """  # noqa: DAR103
    return a + b
