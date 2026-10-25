#Brandon-lee Ouellet Daraiche | 6336739 | nibra37
import json

class Entree:
    def __init__(self,email,mot_de_passe):
        self.email = email
        self.mot_de_passe = mot_de_passe

    def to_dict(self):
        """Convertir l'objet Person en dictionnaire"""
        return {
            'email': self.email,
            'mot_de_passe': self.mot_de_passe
        }

    @classmethod
    def from_dict(cls, data):
        """Créer un objet Person depuis un dictionnaire"""
        return cls(
            email=data['email'],
            mot_de_passe=data['mot_de_passe'])

class Storage:

    def __init__(self, chemin):
        self.chemin = chemin



    def charger_donnees(self):
        try:
            with open(self.chemin, "r", encoding="utf-8") as f:
                loaded_data = json.load(f)

        except FileNotFoundError:
            return []
        except PermissionError:
            raise ValueError("vous n'avez pas les permissions")

        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to decode JSON: {e}")

        except UnicodeDecodeError as e:
            raise ValueError("mauvais decodeur")

        except Exception as e:
            raise ValueError(f"Une erreur est survenue : {e}")

        if not isinstance(loaded_data, list):
            raise ValueError("Le fichier doit contenir une liste.")

        utilisateurs = []
        for data in loaded_data:
            try:
                utilisateurs.append(Entree.from_dict(data))
            except (KeyError, TypeError):
                raise ValueError("Une entrée du fichier est mal formé")
        return utilisateurs

    def sauvegarder_donnees(self,entrees):
        donnees = []
        for donnee in entrees:
            donnees.append(donnee.to_dict())
        with open(self.chemin, "w", encoding="utf-8") as f:
            json.dump(donnees, f, indent=4)

