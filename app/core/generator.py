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
        liste_tous_caracteres = []
        nombre_longueur_mot_de_passe = self.longueurPassword
        if self.minuscule:
            for i in range(nombre_longueur_mot_de_passe):
                minuscule.append(random.choice(string.ascii_lowercase))


        if self.majuscule:
            for i in range(nombre_longueur_mot_de_passe):
                majuscule.append(random.choice(string.ascii_uppercase))

        if self.symbole:
            for i in range(nombre_longueur_mot_de_passe):
                symbole.append(random.choice(string.punctuation))

        if self.chiffre:
            for i in range(nombre_longueur_mot_de_passe):
                chiffre.append(random.choice(string.digits))


        liste_tous_caracteres = minuscule + majuscule + chiffre + symbole
        liste_mot_de_passe = random.choices(liste_tous_caracteres, k=self.longueurPassword)

        random.shuffle(liste_mot_de_passe)
        resultat = "".join(liste_mot_de_passe)

        return resultat