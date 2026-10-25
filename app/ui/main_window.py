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
            email_cachee = QLabel()
            mot_de_passe_cachee = QLabel()
            email_cachee.setText(entree.email)
            mot_de_passe_cachee.setText("*" * len(entree.mot_de_passe))
        #       créer un QLabel avec l'e-mail et des astérisques
        #       (même idée que "*" * len(...) dans ton générateur)
            layout.addWidget(email_cachee)
            layout.addWidget(mot_de_passe_cachee)
        #       l'ajouter au layout du conteneur
        # 3) donner le conteneur à la zone : self.zone.setWidget(conteneur)
        layout.addStretch(1)
        self.zone.setWidget(conteneur)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())