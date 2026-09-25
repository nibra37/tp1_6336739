from app.core.generator import PasswordGenerator
def main() :
    passwordGenerator1 = PasswordGenerator(4,True,True,True,True,True,)
    passwordGenerator2 = PasswordGenerator(9,True,False,False,True,True,)

    print(passwordGenerator1.generateurMotDePasse())
    print(passwordGenerator2.generateurMotDePasse())

if __name__ == '__main__':
   main()


