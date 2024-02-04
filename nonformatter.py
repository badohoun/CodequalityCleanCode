# "espace" pas nécessaire mais présent


def aidemoisurce_sujet(sujet: str) -> None:
    print(sujet)


context_premier_sujet________________ = "Software engineering"
context_deuxieme_sujet_____ = "Data Engineering"
context_troisieme_sujet__ = "Data science"

ressources_surles_sujets = {
    "ressource_softwareengineer________________": 1,
    "ressource_dataengineer_____": 2,
    "ressource_datascience": 3,
}

# de très long lignes de codes
variable = "bonjour"
variable.strip("a").strip("b").strip("c").strip("d").strip("c").strip("e").strip(
    "f"
).strip("g").strip("h").strip("k")


def tropde_variables(
    a: int, b: int, c: int, d: int, e: int, f: int, g: int, i: int, j: int
) -> int:
    return sum(a, b, c, d, e, f, g, i, j)


# l'appel de ma fonction tropde_variables a trop d'espaces cela peut générer des conflits  de merge
tropde_variables(a=139, b=290, c=34, d=354, e=25, f=86, g=7, h=8, i=9, j=200)
