#Brandon-Lee Ouellet Daraiche 6336739 nibra37
import sys

from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QApplication, QWidget, QHBoxLayout,
    QSlider, QSpinBox, QCheckBox, QVBoxLayout, QPushButton, QLabel, QMessageBox, QDialog, QDialogButtonBox
)
from PySide6.QtCore import Qt
from app.core.generator import PasswordGenerator


class Generator_Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("generateur mot de passe")
        self.resize(500, 300)
        self.mot_de_passe = ""
        self.mdp_visible = False
        self.init_ui()

    def init_ui(self):

        layoutV = QVBoxLayout()
        rangee1 = QHBoxLayout()
        rangee2 = QHBoxLayout()
        self.label_mdp = QLabel("*************")
        self.label_mdp.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.label_mdp.setFont(QFont("Courier New", 18))


        self.bouton_copier = QPushButton("Copier")
        self.bouton_copier.clicked.connect(self.copier)

        self.bouton_afficher = QPushButton("afficher")
        self.bouton_afficher.toggled.connect(self.afficher_mot_de_passe)
        self.spin_box = QSpinBox()
        self.bouton_afficher.setCheckable(True)
        rangee1.addWidget(self.label_mdp)
        rangee1.addWidget(self.bouton_copier)
        rangee1.addWidget(self.bouton_afficher)
        layoutV.addLayout(rangee1)

        self.longueur = QLabel("longueur")
        rangee2.addWidget(self.longueur)

        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(4, 20)
        self.slider.setValue(16)
        self.slider.valueChanged.connect(self.spin_box.setValue)
        rangee2.addWidget(self.slider)


        self.spin_box.setRange(4, 20)
        self.spin_box.setValue(16)
        self.spin_box.valueChanged.connect(self.slider.setValue)
        rangee2.addWidget(self.spin_box)
        layoutV.addLayout(rangee2)

        self.checkbox_symbole = QCheckBox("Symbole")
        self.checkbox_symbole.setChecked(True)

        layoutV.addWidget(self.checkbox_symbole)

        self.checkbox_majuscule = QCheckBox("Majuscule")
        self.checkbox_majuscule.setChecked(True)

        layoutV.addWidget(self.checkbox_majuscule)

        self.checkbox_minuscule = QCheckBox("Minuscule")
        self.checkbox_minuscule.setChecked(True)
        layoutV.addWidget(self.checkbox_minuscule)

        self.checkbox_chiffre = QCheckBox("Chiffre")
        self.checkbox_chiffre.setChecked(True)
        layoutV.addWidget(self.checkbox_chiffre)

        self.button_generer_mot_de_passe = QPushButton("generer un mot de passe")
        layoutV.addWidget(self.button_generer_mot_de_passe)
        self.button_generer_mot_de_passe.clicked.connect(self.generer)

        boutons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        boutons.accepted.connect(self.accept)
        boutons.rejected.connect(self.reject)

        layoutV.addWidget(boutons)

        self.setLayout(layoutV)

        self.generer()

    def afficher_mot_de_passe(self, mdp_visible : bool):
        self.mdp_visible = mdp_visible
        self.rafraichir_la_page()


    def rafraichir_la_page(self):
        if self.mdp_visible:
            self.bouton_afficher.setText("masquer")
            self.label_mdp.setText(self.mot_de_passe)
        if not self.mdp_visible:
            self.bouton_afficher.setText("afficher")
            longueur = len(self.mot_de_passe)
            mot_de_passe_cachee = ("*" * longueur)
            self.label_mdp.setText(mot_de_passe_cachee)

    def copier(self):
        texte_copier = QApplication.clipboard()
        texte_copier.setText(self.mot_de_passe)

    def generer(self):


        longueur = self.slider.value()
        symbole = self.checkbox_symbole.isChecked()
        majuscule = self.checkbox_majuscule.isChecked()
        minuscule = self.checkbox_minuscule.isChecked()
        chiffre = self.checkbox_chiffre.isChecked()
        try:
            password_generateur = PasswordGenerator(longueur,minuscule,majuscule,chiffre,symbole,False)
            mot_de_passe_generer = password_generateur.generateur_mot_de_passe()
            self.mot_de_passe = mot_de_passe_generer
            self.rafraichir_la_page()
        except ValueError as erreur:
            QMessageBox.warning(self, "La liste ne peut pas etre vide", "La liste ne peut pas etre vide")




    def get_mot_de_passe(self):
        return self.mot_de_passe




