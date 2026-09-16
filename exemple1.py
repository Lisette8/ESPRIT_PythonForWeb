produit = "pc portable"
prix = 123.4
stock = False

# format
msg = "le produit {} , son prix {} , disponibilitée {}".format(produit, prix, stock)
print(msg)

msg2 = f"le produit {produit} , son prix {prix} , disponibilitée {stock}"
print(msg2)

msg3 = (
    f"produit : {produit.upper()}\n"
    f"prix : {prix}\n"
    f"disponibilitée : {'En stock ' if stock == True else "Rupture"} \n"
)


# boucles et tableaux
prix_TTC = [250.9, 457.99, 89, 100, 98.8]
res = []

for index in prix_TTC:
    res.append(round(index/1.19))

print(res)






