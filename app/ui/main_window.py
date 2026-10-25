#Brandon-Lee Ouellet Daraiche | 6336739 | nibra37
import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QScrollArea, QLabel
)
from app.core.storage import Storage


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

        self.setLayout(layout_principal)
        self.afficher_entrees()

    def afficher_entrees(self):
        # 1) créer un QWidget "conteneur" avec son QVBoxLayout
        conteneur = QWidget()
        layout = QVBoxLayout(conteneur)
        # 2) pour chaque entrée de self.entrees :
        for entree in self.entrees:
            infos_utilisateur = Ligne_entree(entree)
            layout.addWidget(infos_utilisateur)

        layout.addStretch(1)
        self.zone.setWidget(conteneur)

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






if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())