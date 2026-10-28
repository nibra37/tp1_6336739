#Brandon-lee Ouellet Daraiche | 6336739 | nibra37

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


        if self.minuscule:
            liste_tous_caracteres += list(string.ascii_lowercase)

        if self.majuscule:
            liste_tous_caracteres += list(string.ascii_uppercase)

        if self.chiffre:
            liste_tous_caracteres += list(string.digits)

        if self.symbole:
            liste_tous_caracteres += list(string.punctuation)

        if not liste_tous_caracteres:
            raise ValueError("Sélectionnez au moins un type de caractères.")

        nb_types = sum([self.minuscule, self.majuscule, self.chiffre, self.symbole])
        if self.validation and self.longueurPassword < nb_types:
            raise ValueError("Longueur trop petite pour inclure tous les types.")

        mot_de_passe = "".join(random.choices(liste_tous_caracteres, k=self.longueurPassword))

        while self.validation and not self.validation_mot_de_passe(mot_de_passe):
            mot_de_passe = "".join(random.choices(liste_tous_caracteres, k=self.longueurPassword))

        return mot_de_passe

    def validation_mot_de_passe(self, mot_de_passe):
        symboles = string.punctuation
        v_minuscule = any(c.islower() for c in mot_de_passe)
        v_majuscule = any(c.isupper() for c in mot_de_passe)
        v_chiffre = any(c.isdigit() for c in mot_de_passe)
        v_symbole = any(c in symboles for c in mot_de_passe)

        if self.minuscule and not v_minuscule:
            return False
        if self.majuscule and not v_majuscule:
            return False
        if self.chiffre and not v_chiffre:
            return False
        if self.symbole and not v_symbole:
            return False
        return True
