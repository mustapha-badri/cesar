import sys 


mot = input("Saisissez une phrase ou un mot : ")
mot = mot.lower()
mot_decale = ""
decalage = input("Saisissez un décalage : ")


if decalage.isnumeric() == False:
    print("Le décalage est invalide.")
    sys.exit()

valeur_decalage = {
    "a" : 0,
    "b" : 1,
    "c" : 2,
    "d" : 3,
    "e" : 4,
    "f" : 5,
    "g" : 6,
    "h" : 7,
    "i" : 8,
    "j" : 9,
    "k" : 10,
    "l" : 11,
    "m" : 12,
    "n" : 13,
    "o" : 14,
    "p" : 15,
    "q" : 16,
    "r" : 17,
    "s" : 18,
    "t" : 19,
    "u" : 20,
    "v" : 21,
    "w" : 22,
    "x" : 23,
    "y" : 24,
    "z" : 25,

}

lettres_separees = list(mot)

for i in range(len(lettres_separees)):

    if lettres_separees[i].isalpha():
        remplacement = ""
        while remplacement == "":
            for x in valeur_decalage:
                if x == lettres_separees[i]:
                    valeur = (valeur_decalage[x] + int(decalage)) % 26
                    break
            for y in valeur_decalage:
                if valeur_decalage[y] == valeur:
                    remplacement = y
                    lettres_separees[i] = remplacement

    elif lettres_separees[i].isnumeric():
        remplacement = 0
        while remplacement == 0:
            remplacement = int(lettres_separees[i]) + int(decalage)
            lettres_separees[i] = remplacement
            lettres_separees[i] = str(lettres_separees[i])

mot_decale = "".join(lettres_separees)

print(mot_decale)
