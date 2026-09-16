#les methodes (fonctions)

#sans parametres
def saluer():
    return "salut"

print(saluer())


#avec parametres
def saluer(name) -> str:
    return "salut "+name

print(saluer("iyed"))


#avec valeurs par défauts
def saluer(name="iyed") -> str:
    return "salut "+name

print(saluer())


def somme(produit_nom,  *nombres):
    res = sum(nombres)
    return f"product name is {produit_nom} with total price {price}"

print(somme("pc portable", 10, 90, 9, 89, 100))