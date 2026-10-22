import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QHBoxLayout,
    QComboBox, QListWidget, QSlider, QSpinBox, QDial, QCheckBox, QVBoxLayout, QPushButton, QLabel
)
from PySide6.QtCore import Qt  # Pour l'orientation du slider


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("generateur mot de passe")
        self.resize(500, 100)  # Taille initiale

        # Création du layout horizontal
        layoutV = QVBoxLayout()
        rangee1 = QHBoxLayout()
        rangee2 = QHBoxLayout()
        # Ajout des widgets (alignés horizontalement)
        self.label_mdp = QLabel("*************")
        self.bouton_copier = QPushButton("Copier")
        self.bouton_afficher = QPushButton("afficher")
        rangee1.addWidget(self.label_mdp)
        rangee1.addWidget(self.bouton_copier)
        rangee1.addWidget(self.bouton_afficher)
        layoutV.addLayout(rangee1)

        rangee2.addWidget(QLabel("longueur"))
        layoutV.addLayout(rangee2)

        slider = QSlider(Qt.Orientation.Horizontal)
        slider.setRange(4, 20)  # Valeurs de 0 à 100
        slider.setValue(4)  # Valeur initiale
        rangee2.addWidget(slider)



        spinBox = QSpinBox()
        spinBox.setRange(4, 20)
        spinBox.setValue(4)
        rangee2.addWidget(spinBox)
        layoutV.addLayout(rangee2)

        checkbox = QCheckBox("Symbole")
        checkbox.stateChanged.connect(lambda: print("État:", checkbox.isChecked()))
        layoutV.addWidget(checkbox)

        checkbox = QCheckBox("Majuscule")
        checkbox.stateChanged.connect(lambda: print("État:", checkbox.isChecked()))
        layoutV.addWidget(checkbox)

        checkbox = QCheckBox("Minuscule")
        checkbox.stateChanged.connect(lambda: print("État:", checkbox.isChecked()))
        layoutV.addWidget(checkbox)

        checkbox = QCheckBox("Chiffre")
        checkbox.stateChanged.connect(lambda: print("État:", checkbox.isChecked()))
        layoutV.addWidget(checkbox)

        button = QPushButton("generer un mot de passe")
        layoutV.addWidget(button)
        button.clicked.connect(lambda: print("Bouton cliqué !"))
        # Application du layout à la fenêtre
        self.setLayout(layoutV)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())