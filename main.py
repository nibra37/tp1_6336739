#Brandon-lee Ouellet Daraiche | 6336739 | nibra37
from PySide6.QtWidgets import QApplication

from app.core.generator import PasswordGenerator
import argparse
import PySide6
import sys
from app.ui.main_window import MainWindow

def main():
    parser = argparse.ArgumentParser(description="gestionnaire mot de passe")
    parser.add_argument("--length", type=int, default = 16)
    parser.add_argument("--no-lower", action="store_true")
    parser.add_argument("--no-upper", action="store_true")
    parser.add_argument("--no-digits", action="store_true")
    parser.add_argument("--no-symbols", action="store_true")
    parser.add_argument("--validate", action="store_true")
    parser.add_argument("--no-gui", action="store_true")
    parser.add_argument("--vault_file", default="vault.json")
    args = parser.parse_args()

    if args.no_gui:
        try:
            passwordGenerator = PasswordGenerator(args.length, not args.no_lower, not args.no_upper, not args.no_digits,
                                                  not args.no_symbols, args.validate)
            print(passwordGenerator.generateur_mot_de_passe())
        except ValueError as e:
            print(str(e))
    else:
        app = QApplication(sys.argv)
        fenetre = MainWindow(args.vault_file)
        fenetre.show()
        sys.exit(app.exec())




if __name__ == '__main__':
    main()
