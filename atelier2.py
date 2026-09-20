# POO

#exemple 1
class Personne():
    def __init__(self, nom: str, age: int):
        self.nom = nom
        self.age = age
    
    def se_presenter(self):
        print("Je m'appelle {} et j'ai {} ans.".format(self.nom, self.age)) 
    
p1 = Personne("Alice", 30)
p1.se_presenter()


#exemple 2
class Personne():
    def __init__(self, nom: str, age: int):
        self.nom = nom
        self.age = age
    
    def se_presenter(self):
        print("Je m'appelle {} et j'ai {} ans.".format(self.nom, self.age)) 
    
    def __str__(self):
        return ("Je m'appelle {} et j'ai {} ans.".format(self.nom, self.age))

p1 = Personne("Alice", 30)
print(p1.__str__())


#exemple 3
class Etudiant(Personne):
    def __init__(self, nom, age, niveau: str):
        super().__init__(nom, age)
        self.niveau = niveau

    def etudier(self):
        print("je suis en {} et j'étudie dur!".format(self.niveau))

e1 = Etudiant("Bob", 20, "Master")
e1.se_presenter()
e1.etudier()


#exemple 5
class Panier():
    def __init__(self, articles: list[str]):
        self.articles = articles

    def __len__(self):
        return len(self.articles)
    
p1 = Panier(["pomme", "banane"])
print("la longeur du panier est:", p1.__len__())


#exemple 6
class Panier():
    def __init__(self, articles: list[str]):
        self.articles = articles

    def __len__(self):
        return len(self.articles)
    
    def __getitem__(self, index):
        return self.articles[index]
    
p1 = Panier(["pomme", "banane"])
print("le premier article de ce panier est:", p1.__getitem__(0))


#exemple 7
class Produit():
    def __init__(self, nom: str, prix: float):
        self.nom = nom
        self.prix = prix

    def __eq__(self, value):
        return self.nom == value
    
prod1 = Produit("Livre", 10.0)
prod2 = Produit("Livre", 15.0)

print(prod1.__eq__(prod2))


#exemple 8
class Point():
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, value):
        return Point(self.x + value.x, self.y+value.y)
    
    def __str__(self):
        return "({},{})".format(self.x, self.y)

    
p1 = Point(1, 2)
p2 = Point(3, 4)


print(p1.__str__())
print(p2.__str__())
print(p1 + p2)



#exemple 9
class Personne():
    def __init__(self, nom: str, age: int):
        self.nom = nom
        self.age = age
    
    def se_presenter(self):
        print("Je m'appelle {} et j'ai {} ans.".format(self.nom, self.age)) 
    
    def __str__(self):
        return ("Je m'appelle {} et j'ai {} ans.".format(self.nom, self.age))
    
    def __del__(self):
        return "{} a été détruit.".format(self.nom)

p1 = Personne("Charlie", 25)
print(p1.__del__())




# PARTIE 3 : ETUDE DE CAS

# 1

class Livre():
    def __init__(self, titre: str, auteur: str, annee: int, disponible: bool = True):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.disponible = disponible

    def emprunter(self):
        if self.disponible == True:
            self.disponible = False
            return "Livre emprunté !"
        else:
            return "Indisponible"

    def retourner(self):
        self.disponible = True
        return "Livre retourné !"
    
    def __str__(self):
        return "Titre : {}, Auteur : {}, Annee : {}, Disponible : {}".format(self.titre, self.auteur, self.annee, "oui" if self.disponible else "non")



class Roman(Livre):
    def __init__(self, genre: str, titre, auteur, annee, disponible = True):
        super().__init__(titre, auteur, annee, disponible)
        self.genre = genre

    def __str__(self):
        return f"{super().__str__()}, Genre : {self.genre}."
    


class Bibliotheque():
    def __init__(self, livres: list[Livre] = None):
        self.livres = livres
    
    def ajouter_livre(self, livre: Livre):
        self.livres.append(livre)

    def lister_livres(self):
        livres = []
        for livre in self.livres:
            livres.append(str(livre))   
        return livres
        
    def emprunter_livre(self, titre: str):
        for livre in self.livres:
            if livre.titre == titre:
                return livre.emprunter()
            
        return "Livre non trouvé."
            

l1 = Livre("titre1", "iyed1", 2004, True)
r1 = Roman("Policier", "titre1", "iyed1", 2004, True) 
b1 = Bibliotheque([l1, r1])   

print(l1.emprunter())
print(b1.lister_livres())
print(l1.retourner())
print(b1.lister_livres())