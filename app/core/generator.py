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

    def generateur_mot_de_passe(self):
        liste_tous_caracteres = []
        mot_de_passe = []

        if self.minuscule:
            liste_tous_caracteres += list(string.ascii_lowercase)
            mot_de_passe.append(random.choice(string.ascii_lowercase))

        if self.majuscule:
            liste_tous_caracteres += list(string.ascii_uppercase)
            mot_de_passe.append(random.choice(string.ascii_uppercase))

        if self.chiffre:
            liste_tous_caracteres += list(string.digits)
            mot_de_passe.append(random.choice(string.digits))

        if self.symbole:
            liste_tous_caracteres += list(string.punctuation)
            mot_de_passe.append(random.choice(string.punctuation))

        # Compléter le reste du mot de passe aléatoirement
        taille_restante = self.longueurPassword - len(mot_de_passe)
        mot_de_passe += random.choices(liste_tous_caracteres, k=max(0, taille_restante))

        random.shuffle(mot_de_passe)
        resultat = "".join(mot_de_passe[:self.longueurPassword])

        if self.validation:
            self.validation_mot_de_passe(resultat)

        return resultat

    def validation_mot_de_passe(self, mot_de_passe):
        symboles = string.punctuation
        v_minuscule = any(c.islower() for c in mot_de_passe)
        v_majuscule = any(c.isupper() for c in mot_de_passe)
        v_chiffre = any(c.isdigit() for c in mot_de_passe)
        v_symbole = any(c in symboles for c in mot_de_passe)

        if v_minuscule and v_majuscule and v_chiffre and v_symbole:
            print("Vous avez un caractère de chaque catégorie")
        else:
            print("Vous n'avez pas un caractère de chaque catégorie")
