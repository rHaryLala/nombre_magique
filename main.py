import random

def demander_nombre(nb_min, nb_max):
    nombre_int = 0
    while nombre_int == 0:
        nombre_str = input(f"Quel est le nombre magique ? (entre {nb_min} et {nb_max}) ")
        try:
            nombre_int = int(nombre_str)
        except :
            print("ERREUR: Veuillez entrer un nombre valide !")
        else:
            if nombre_int < nb_min or nombre_int > nb_max:
                print(f"Veuillez entrer un nombre entre {nb_min} et {nb_max}")
                nombre_int = 0
    return nombre_int



NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN, NOMBRE_MAX)
NB_VIES = 4


# Nombre
nb = 0
vies = NB_VIES
while not nb == NOMBRE_MAGIQUE and vies > 0:
    print(f"Il vous reste {vies} vies")
    nb = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
    if nb < NOMBRE_MAGIQUE:
        print("le nombre magique est plus grand")
    elif nb > NOMBRE_MAGIQUE:
        print("Le nombre magique est plus petit")
        vies -= 1
    else:
        print("\n Bravo, vous ave gagné")

if vies == 0:
    print("\n Vous avez perdu")
