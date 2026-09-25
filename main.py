from app.core.generator import PasswordGenerator
def main() :
    passwordGenerator1 = PasswordGenerator(4,True,True,True,True,True,)
    passwordGenerator2 = PasswordGenerator(9,True,True,False,True,True,)

    print(passwordGenerator1.generateur_mot_de_passe())
    print(passwordGenerator2.generateur_mot_de_passe())

if __name__ == '__main__':
   main()


