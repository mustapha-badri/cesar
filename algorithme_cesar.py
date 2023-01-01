import sys 


mot = input("Saisissez une phrase ou un mot : ")
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
    "A" : 36,
    "B" : 37,
    "C" : 38,
    "D" : 39,
    "E" : 40,
    "F" : 41,
    "G" : 42,
    "H" : 43,
    "I" : 44,
    "J" : 45,
    "K" : 46,
    "L" : 47,
    "M" : 48,
    "N" : 49,
    "O" : 50,
    "P" : 51,
    "Q" : 52,
    "R" : 53,
    "S" : 54,
    "T" : 55,
    "U" : 56,
    "V" : 57,
    "W" : 58,
    "X" : 59,
    "Y" : 60,
    "Z" : 61,
    "0" : 26,
    "1" : 27,
    "2" : 28,
    "3" : 29,
    "4" : 30,
    "5" : 31,
    "6" : 32,
    "7" : 33,
    "8" : 34,
    "9" : 35,
}

lettres_separees = list(mot)

for i in range(len(lettres_separees)):

    if (lettres_separees[i].isalpha() == True) or (lettres_separees[i].isnumeric() == True):
        remplacement = ""
        while remplacement == "":
            for x in valeur_decalage:
                if x == lettres_separees[i]:
                    valeur = (valeur_decalage[x] + int(decalage)) % len(valeur_decalage)
                    break
            for y in valeur_decalage:
                if valeur_decalage[y] == valeur:
                    remplacement = y
                    lettres_separees[i] = remplacement

mot_decale = "".join(lettres_separees)

print(mot_decale)
