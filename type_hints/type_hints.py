from typing import (
    Dict,
    List,
    NamedTuple,
    Optional,
    Set,
    Tuple,
    Type,
    TypedDict,
    Union,
)

# bonjourexemple: int = 1
# bonjourexemple = "bonjour"


# def utiliser_plusieurs_types(
# num: int,
# decimal: float,
# boolean: bool,
# string: str,
# binary: bytes,
# obj: object,
# ) -> None: ...


# Première option
# Point = NamedTuple("Point", ["x" , "y"])

# point2d = Point(1,2)
# Point = namedtuple("Point", ["x" , "y"]) # on fournit une liste de x et y en entrée
# point2d = Point(1, 2) #  une instance de la classe Point avec les coordonnées x et y (subclass de tuple mais on peut le traiter comme tuple)
# point2d.x
# point2d.y


# deuxièmle option
class Point(NamedTuple):
    x: int
    y: int


# point2d = Point(1, 2)
#  une instance de la classe Point avec les coordonnées x et y (subclass de tuple mais on peut le traiter comme tuple)
# point2d.x
# point2d[0]


class Student2(
    TypedDict
):  # a student2 est la composition de types simples primitives(name, age) et types complexes position
    name: str
    age: int
    position: Point


etudiants2: Student2 = {
    "name": "Paul",
    "age": 20,
    "position": Point(1, 2),
}

autre_etudiant = Student2(name="Samuel", age=25, position=(4, 42))
print(autre_etudiant)
# pas valable built-in list class type python < 3.9 (list of int ) ie python 3.8
# pour des contraintes de productions vous devez écrire dans des versions qui sont disponible dans les environnements de productions clouds
# votre code doit etre portable
# un autre type plus large pour definir un type dict est mapping
# mais la best practice est d'utiliser les types spécifiques les plus étroits "narrow type"
# type Sequence impliquent que les types de données sont ordonnées
# Liste et tuples sont des narrows type de sequences
# Iterable : tout type de collections de scalaires par exemple set
#
num: List[int] = [4, 2, 6, 8]
numeros: List[int] = [1, 2, 3, 4]
vecteurs_a_trois_dimensions: tuple[int, float, str] = (1, 2.0, "hi")
vecteurs_a_n_dimensions: Tuple[float, ...] = 1, 2, 3, 4, 5

ages_etudiants: Dict[str, int] = {
    "bobby": 25,
    "murph": 27,
    "alice": 21,
}


fruits: Set[str] = {"pomme", "mangue", "banane"}

# méthodes publiques fruits.

# fruits.


# type itself ou un type lui meme
# gecko est de type x
class Animal: ...


# xvalues = Animal
# gecko = x()
# gecko


valeur_mak: List[Union[int, float, str, Type]] = [1, 1.0, "hi", object, str, "hi"]

valeur_mak: List[int | float | str | Type] = [1, 1.0, "hi", object]

x_value: Union[int, float, str, Type] = (
    None  # composition de simples types : c'est un type complexe
)
x_value: int | float | str | Type = (
    None  # cette méthode est plus claire et plus performante
)
# mais il y'a des soucis de compatibilité  en fonction de votre version de python
# donc je vous invite à utiliser dans vos projets pour plus de  sureté

# dès fois on a besoin d'initialiser une valeur
# mais on ne sait pas encore quelle type il va prendre par la suite
# donc on peut faire x = None  ou x : Optional

# x: Union[int, None] = None
# x: Optional[int] = None


def greet(name: Optional[str] = None):
    if not name:
        print("Hello!")
        return
    print(f"Hello, {name}!")


# etudiant : Dict[str, Union[str, int]]
# etudiant = {
# "name": "Marie",
# "age":25
# }


class Student(TypedDict):
    name: str
    age: int


etudiants: Student = {"name": "Paul", "age": 20}

# etudiants[]

# l'autocomplétion des dictionnaires possible avec le typeDict
# utile énormément
# pour les data engioneers qui ont besoin de déplacer de la data sous différents formats

# on peut utiliser le typeDict definition pour instancier
other_student = Student(name="Samuel", age=25)

print(other_student)


class Duck:
    def __init__(self): ...

    def __getattribute__(self, attr: str):
        if attr == "quack":
            return lambda: print("quack")
        elif attr == "swim":
            return lambda: print("splash")
        else:
            raise AttributeError


duck = Duck()

duck.quack()


from pathlib import Path

e = 1
