def grand_nombre(n):
    return f"{n:_}".replace("_", " ")


def multiplication(n1: int, n2: int):
    etages = []
    # présenter la multiplication correctement : le plus grand au-dessus
    terme1, terme2 = (n2, n1) if n2 > n1 else (n1, n2)
    puissance = 1

    # résultats des étages
    for i in reversed(str(terme2)):
        result = int(i) * terme1 * puissance
        etages.append(result)
        # multiplie par 10 chaque étage
        puissance *= 10

    resultat = sum(etages)

    # mise en page
    largeur = len(grand_nombre(resultat)) + 2

    print(f"{grand_nombre(terme1):>{largeur}}")
    print(f"x {grand_nombre(terme2):>{largeur -2}}")
    print("─" * largeur)

    if len(etages) > 1:
        print(f"{grand_nombre(etages[0]):>{largeur}}")
        for i in etages[1:]:
            print(f"+ {grand_nombre(i):>{largeur -2}}")
        print("─" * largeur)

    print(f"{grand_nombre(resultat):>{largeur}}")


def demander_nombre(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Veuillez entrer un nombre valide.")


while True:
    n1 = demander_nombre("Première valeur (0 pour quitter) : ")
    if n1 == 0:
        break
    n2 = demander_nombre("Deuxième valeur (0 pour quitter) : ")
    if n2 == 0:
        break

    multiplication(n1, n2)
    print()
