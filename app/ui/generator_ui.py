import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QHBoxLayout,
    QSlider, QSpinBox, QCheckBox, QVBoxLayout, QPushButton, QLabel
)
from PySide6.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("generateur mot de passe")
        self.resize(800, 200)
        self.init_ui()

    def init_ui(self):

                    layoutV = QVBoxLayout()
                    rangee1 = QHBoxLayout()
                    rangee2 = QHBoxLayout()
                    self.label_mdp = QLabel("*************")
                    self.label_mdp.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

                    self.bouton_copier = QPushButton("Copier")

                    self.bouton_afficher = QPushButton("afficher")
                    self.bouton_afficher.setCheckable(True)
                    rangee1.addWidget(self.label_mdp)
                    rangee1.addWidget(self.bouton_copier)
                    rangee1.addWidget(self.bouton_afficher)
                    layoutV.addLayout(rangee1)

                    self.longueur = QLabel("longueur")
                    self.slider = QSlider(Qt.Orientation.Horizontal)
                    rangee2.addWidget(self.longueur)



                    self.slider.setRange(4, 20)
                    self.slider.setValue(16)
                    rangee2.addWidget(self.slider)



                    self.spin_box = QSpinBox()
                    self.spin_box.setRange(4, 20)
                    self.spin_box.setValue(16)
                    rangee2.addWidget(self.spin_box)
                    layoutV.addLayout(rangee2)

                    self.checkbox_symbole = QCheckBox("Symbole")
                    self.checkbox_symbole.setChecked(True)
                    self.checkbox_symbole.stateChanged.connect(lambda: print("État:", self.checkbox_symbole.isChecked()))
                    layoutV.addWidget(self.checkbox_symbole)

                    self.checkbox_majuscule = QCheckBox("Majuscule")
                    self.checkbox_majuscule.setChecked(True)
                    self.checkbox_majuscule.stateChanged.connect(lambda: print("État:", self.checkbox_majuscule.isChecked()))
                    layoutV.addWidget(self.checkbox_majuscule)

                    self.checkbox_minuscule = QCheckBox("Minuscule")
                    self.checkbox_minuscule.setChecked(True)
                    self.checkbox_minuscule.stateChanged.connect(lambda: print("État:", self.checkbox_minuscule.isChecked()))
                    layoutV.addWidget(self.checkbox_minuscule)

                    self.checkbox_chiffre = QCheckBox("Chiffre")
                    self.checkbox_chiffre.setChecked(True)
                    self.checkbox_chiffre.stateChanged.connect(lambda: print("État:", self.checkbox_chiffre.isChecked()))
                    layoutV.addWidget(self.checkbox_chiffre)

                    self.button_generer_mot_de_passe = QPushButton("generer un mot de passe")
                    layoutV.addWidget(self.button_generer_mot_de_passe)
                    self.button_generer_mot_de_passe.clicked.connect(lambda: print("Bouton cliqué !"))
                    self.setLayout(layoutV)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

