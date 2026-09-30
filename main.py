#Brandon-lee Ouellet Daraiche | 6336739 | nibra37
from app.core.generator import PasswordGenerator
import argparse

import argparse


def main():
    parser = argparse.ArgumentParser(description="gestionnaire mot de passe")
    parser.add_argument("--length", type=int)
    parser.add_argument("--no-lower", action="store_false")
    parser.add_argument("--no-upper", action="store_false")
    parser.add_argument("--no-digits", action="store_false")
    parser.add_argument("--no-symbols", action="store_false")
    parser.add_argument("--validate", action="store_true")

    args = parser.parse_args()

    passwordGenerator = PasswordGenerator(args.length, args.no_lower, args.no_upper, args.no_digits, args.no_symbols, args.validate)
    print(passwordGenerator.generateur_mot_de_passe())


if __name__ == '__main__':
    main()
