#1
name = input("donnez votre nom: ")
age = input("donnez votre age: ")

print("Hello {}, you are {} years old.".format(name, age))

#2
nombre = input("donnez un nombre: ")
nombre = int(nombre)
if (nombre > 0):
    if (nombre % 2 == 0):
        print("nombre pair")
    else:
        print("nombre impair")

#3
chaine = "testchaine"
for letter in chaine:
    print(letter, end="") 

somme = 0
for num in range(1, 101):
    somme = somme + num

print("\nLa somme est: ", somme)

#4
notes = [12, 15, 9, 18, 14]
somme = 0
nombre_elements = 0
note_max = max(notes)
note_min = min(notes)
for note in notes:
    nombre_elements = nombre_elements + 1
    somme = somme + note
    
print("Moyenne = {}".format(somme / nombre_elements))
print("Note max = {}".format(note_max))
print("Note min = {}".format(note_min))

#5
student = {
    "name": "Ali", 
    "age": 20,
    "study field": "computer science"
}

student["email"] = None

print(student)

#6
animaux = {"cat", "dog", "bird", "cat"}

print(animaux) 
# le mot cat se répète deux fois et l'affichage final élimine les doublons et affiche selon l'ordre alphabétique

tuple = ("nom", "age", "ville")
for index in tuple:
    print(index)



# 

#exercices d'application

# 1
pays = []
v_pays = None

print("Tapez 0 pour quitter...")
while True:
    v_pays = input("Donnez le pays visité: ")
    
    if(v_pays == ""):
        continue

    if(v_pays != "0"):
        pays.append(v_pays)

    if v_pays == "0":
        break

print("Les pays sont:\n{}".format(pays))

# le nombre d'occurences des pays dans la liste
pays_occurrences = {}

for Pays in pays:
    pays_occurrences[Pays] = pays.count(Pays)

print("Les nombres d'occurences des pays sont: \n{}".format(pays_occurrences))

# le pays le plus visité
pays_plus_visite_occurence = 0
pays_plus_visite = None
for cle, valeur in pays_occurrences.items():
    if pays_plus_visite_occurence < valeur:
        pays_plus_visite_occurence = valeur
        pays_plus_visite = cle

print(pays_plus_visite)


#

# 2

#a

purchases = [
    {"product": "Computer", 'price': 1200, "quantity": 2},
    {"product": "Mouse", 'price': 25, "quantity": 5}, 
    {"product": "Keyboard", 'price': 45, "quantity": 3}, 
    {"product": "Monitor", 'price': 300, "quantity": 2}, 
    {"product": "Mouse", 'price': 25, "quantity": 2},
]   

montant_total_depense = 0

for purchase in purchases:
    for cle, valeur in purchase.items():
        if cle == "price":
            prix = valeur
        elif cle == "quantity":
            quantite = valeur

    montant_total_depense = montant_total_depense + (prix * quantite)


print(montant_total_depense)   
    

#b
purchases_recap = {}

for purchase in purchases:
    product = purchase["product"]
    quantity = purchase["quantity"]

    if product in purchases_recap:
        purchases_recap[product] = purchases_recap[product] + quantity
    else:
        purchases_recap[product] = quantity
    
print(purchases_recap)


#c
max = 0
for cle, valeur in purchases_recap.items():
    if max < valeur:
        max = valeur
        nom_produit = cle

print("le produit le plus acheté est: {}".format(nom_produit))


#d
ventes_totales_par_produit = {}

for cle, valeur in purchases_recap.items():
    for purchase in purchases:
        if purchase["product"] == cle:
            price = purchase["price"]

    ventes_totales_par_produit[cle] = price * valeur

print(ventes_totales_par_produit)



#

# 3

#a
phrase = input("donnez une phrase complete: ")
liste_mots = phrase.split()

#b
print("la liste des mots de cette phrase est: {}".format(liste_mots))

#c
liste_mots.append("incroyable")
print(liste_mots)
phrase = " ".join(liste_mots)

#d
phrase = phrase.replace("puissant", "facile")
print(phrase)
liste_mots = phrase.split()

#e
print(f"le nombre totals des mots dans cette phrase est: {len(liste_mots)}")

#f
nouvelle_phrase = "-".join(liste_mots)

#g
print("nouvelle phrase: {}".format(nouvelle_phrase))

#h
for mot in liste_mots:
    print("Mot {} : {}".format(liste_mots.index(mot)+1, mot.upper()))



