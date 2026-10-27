#Brandon-Lee Ouellet Daraiche | 6336739 | nibra37
import json
import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QScrollArea, QLabel, QDialog, QLineEdit, QDialogButtonBox, QPushButton,
    QMessageBox, QMenu
)
from app.core.storage import Storage,Entree
from app.ui.generator_ui import Generator_Dialog
from PySide6.QtCore import Signal

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Coffre-fort")
        self.resize(500, 400)
        self.storage = Storage("vault.json")
        self.entrees = self.storage.charger_donnees()

        self.init_ui()



    def init_ui(self):
        layout_principal = QVBoxLayout()

        self.zone = QScrollArea()
        self.zone.setWidgetResizable(True)
        layout_principal.addWidget(self.zone)



        self.bouton_ajouter = QPushButton("Ajouter")
        self.bouton_ajouter.clicked.connect(self.ajouter_entree)
        layout_principal.addWidget(self.bouton_ajouter)

        self.bouton_trier = QPushButton("Trier")
        self.bouton_trier.clicked.connect(self.trier_donnees_par_nom)
        layout_principal.addWidget(self.bouton_trier)

        self.setLayout(layout_principal)
        self.afficher_entrees()

    def afficher_entrees(self):
        conteneur = QWidget()
        layout = QVBoxLayout(conteneur)

        for entree in self.entrees:
            infos_utilisateur = Ligne_entree(entree)
            layout.addWidget(infos_utilisateur)
            infos_utilisateur.supprimer_demande.connect(self.supprimer_entree)
            infos_utilisateur.modifier_demande.connect(self.modifier_entree)


        layout.addStretch(1)
        self.zone.setWidget(conteneur)



    def ajouter_entree(self):
        boite = Dialog_entree()
        if boite.exec() == QDialog.DialogCode.Accepted:
            email = boite.get_email()
            mot_de_passe = boite.get_mot_de_passe()

            if email == "":
                pas_email = QMessageBox.warning(boite,"message erreur", "L'email ne peut pas être vide")
                return pas_email
            if mot_de_passe == "":
                pas_mot_de_passe = QMessageBox.warning(boite, "message erreur", "Le mot de passe ne peut pas être vide")
                return pas_mot_de_passe
            entree = Entree(email, boite.get_mot_de_passe())
            self.entrees.append(entree)
            self.storage.sauvegarder_donnees(self.entrees)
            self.afficher_entrees()

    def supprimer_entree(self, entree):
        bouton_supprimer = QMessageBox.question(self, "Confirmation", "Supprimer cette entrée ?")
        if bouton_supprimer == QMessageBox.StandardButton.Yes:
            self.entrees.remove(entree)
            self.storage.sauvegarder_donnees(self.entrees)
            self.afficher_entrees()
        return bouton_supprimer

    def modifier_entree(self, entree):
        boite = Dialog_entree(entree)
        if boite.exec() == QDialog.DialogCode.Accepted:

            email = boite.get_email()
            mot_de_passe = boite.get_mot_de_passe()

            entree.email = email
            entree.mot_de_passe = mot_de_passe

            if email == "":
                pas_email = QMessageBox.warning(boite, "message erreur", "L'email ne peut pas être vide")
                return pas_email
            if mot_de_passe == "":
                pas_mot_de_passe = QMessageBox.warning(boite, "message erreur", "Le mot de passe ne peut pas être vide")
                return pas_mot_de_passe

            self.storage.sauvegarder_donnees(self.entrees)
            self.afficher_entrees()

    def trier_donnees_par_nom(self):
        donnees_trier = sorted(self.entrees, key=lambda e: e.email.lower())
        self.entrees = donnees_trier
        self.afficher_entrees()

class Ligne_entree(QLabel):
    supprimer_demande = Signal(object)
    modifier_demande = Signal(object)

    def __init__(self, entree):
        super().__init__()
        self.entree = entree
        self.revele = False
        self.rafraichir()

    def mouseDoubleClickEvent(self, event):
        self.revele = not self.revele
        self.rafraichir()

    def rafraichir(self):
        if self.revele:
            self.setText(f"{self.entree.email} : {self.entree.mot_de_passe}")
        else:
            self.setText(f"{self.entree.email} :  {'*' * len(self.entree.mot_de_passe)}")


    def contextMenuEvent(self, event):
        menu = QMenu(self)
        afficher = menu.addAction("afficher")
        modifier = menu.addAction("modifier")
        supprimer = menu.addAction("supprimer")
        choix = menu.exec(event.globalPos())
        if choix == afficher:
            self.revele = not self.revele
            self.rafraichir()
        if choix == modifier:
            self.modifier_demande.emit(self.entree)

        if choix == supprimer:
            self.supprimer_demande.emit(self.entree)





class Dialog_entree(QDialog):
    def __init__(self, entree = None):
        super().__init__()
        self.email = QLineEdit()
        self.mot_de_passe =QLineEdit()
        self.setWindowTitle("Ajouter une entrée")
        if entree is not None:
            self.email.setText(entree.email)
            self.mot_de_passe.setText(entree.mot_de_passe)
            self.setWindowTitle("modifier une entrée")

        layout = QVBoxLayout()

        self.email_interface = QLabel("email")

        self.mot_de_passe_interface = QLabel("mot de passe")
        self.bouton_generer = QPushButton("generer")
        self.bouton_generer.clicked.connect(self.ouvrir_generateur)
        boutons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        boutons.accepted.connect(self.accept)
        boutons.rejected.connect(self.reject)

        layout.addWidget(self.email_interface)
        layout.addWidget(self.email)
        layout.addWidget(self.mot_de_passe_interface)
        layout.addWidget(self.mot_de_passe)
        layout.addWidget(self.bouton_generer)
        layout.addWidget(boutons)
        self.setLayout(layout)

    def get_email(self):
        email = self.email.text()

        return email

    def get_mot_de_passe(self):
        mot_de_passe = self.mot_de_passe.text()

        return mot_de_passe

    def ouvrir_generateur(self):
        boite = Generator_Dialog()
        if boite.exec() == QDialog.DialogCode.Accepted:
            mot_de_passe = boite.get_mot_de_passe()
            self.mot_de_passe.setText(mot_de_passe)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())