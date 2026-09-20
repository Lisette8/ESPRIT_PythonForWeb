class Livre:
    def __init__(self, titre:str, auteur:str, prix:float):
        self.titre = titre
        self.auteur = auteur
        self.prix = prix
        self.stock = False

    def __str__(self):
        return f"Titre: {self.titre}\nAuteur: {self.auteur}\nPrix: {self.prix}"
    
    def appliquer_remise(self, taux:float):
        if (0<taux<1):
            self.prix = round(self.prix*(1 - taux), 2)
        return self.prix



l1 = Livre("livre1", "iyed", 10.10)

print(l1)

l1.appliquer_remise(0.5)
print("l1 apres remise::")
print(l1)



#heritage
class Elivre(Livre):
    def __init__(self, titre, auteur, prix, link):
        super().__init__(titre, auteur, prix)
        self.link = link

    def __str__(self):
        return f"{super().__str__()}, avec un lien{self.link}"
    

l2 = Elivre("livre1", "iyed", 10.10, "http://....")
print(l2)