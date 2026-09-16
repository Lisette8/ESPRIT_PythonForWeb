
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
student = {
    "name": "Ali", 
    "age": 20,
    "study field": "computer science"
}

student["email"]= None

print(student)


#5
animaux = {"cat", "dog", "bird", "cat"}