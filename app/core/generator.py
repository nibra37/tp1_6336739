import random
import string


class PasswordGenerator:
    def __init__(self, longueurPassword, minuscule, majuscule, chiffre, symbole, validation):
        self.longueurPassword = longueurPassword
        self.minuscule = minuscule
        self.majuscule = majuscule
        self.chiffre = chiffre
        self.symbole = symbole
        self.validation = validation

    def generateurMotDePasse(self):
        minuscule = []
        majuscule = []
        symbole = []
        chiffre = []

        nombre_random_minuscule = random.randint(1, 3)
        for i in range(nombre_random_minuscule):
            minuscule.append(random.choice(string.ascii_lowercase))

        nombre_random_majuscule = random.randint(1, 3)
        for i in range(nombre_random_majuscule):
            majuscule.append(random.choice(string.ascii_uppercase))

        nombre_random_symbole = random.randint(1, 3)
        for i in range(nombre_random_symbole):
            symbole.append(random.choice(string.punctuation))

        nombre_random_chiffre = random.randint(1, 3)
        for i in range(nombre_random_chiffre):
            chiffre.append(random.choice(string.digits))

        liste_tous_caracteres = minuscule + majuscule + chiffre + symbole
        liste_mot_de_passe = random.choices(liste_tous_caracteres, k=self.longueurPassword)

        random.shuffle(liste_mot_de_passe)
        resultat = "".join(liste_mot_de_passe)

        return resultat