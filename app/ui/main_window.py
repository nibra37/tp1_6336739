#Brandon-Lee Ouellet Daraiche | 6336739 | nibra37
import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QScrollArea, QLabel, QDialog, QLineEdit, QDialogButtonBox, QPushButton,
    QMessageBox
)
from app.core.storage import Storage,Entree


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Coffre-fort")
        self.resize(500, 400)
        self.storage = Storage("test2.json")
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

        self.setLayout(layout_principal)
        self.afficher_entrees()

    def afficher_entrees(self):
        conteneur = QWidget()
        layout = QVBoxLayout(conteneur)

        for entree in self.entrees:
            infos_utilisateur = Ligne_entree(entree)
            layout.addWidget(infos_utilisateur)

        layout.addStretch(1)
        self.zone.setWidget(conteneur)



    def ajouter_entree(self):
        boite = Dialog_entree()
        if boite.exec() == QDialog.DialogCode.Accepted:
            email = boite.get_email()

            if email == "":
                pas_email = QMessageBox.warning(boite,"message erreur", "L'email ne peut pas être vide")
                return pas_email
            entree = Entree(email, boite.get_mot_de_passe())
            self.entrees.append(entree)
            self.storage.sauvegarder_donnees(self.entrees)
            self.afficher_entrees()



class Ligne_entree(QLabel):
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



class Dialog_entree(QDialog):
    def __init__(self):
        super().__init__()
        self.email = QLineEdit()
        self.mot_de_passe =QLineEdit()
        self.setWindowTitle("Ajouter une entrée")


        layout = QVBoxLayout()

        self.email_interface = QLabel("email")

        self.mot_de_passe_interface = QLabel("mot de passe")
        self.bouton_generer = QPushButton("generer")
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())