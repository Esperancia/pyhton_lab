from Tools.Polynomial import Polynomial
from Tools.Term import Term


class ConsoleApp:

    def __init__(self):
        self.polynomes = []

    def initListePolynome(self):
        t0 = Term("t0", 3.0, 'x', 2)  # 3x^2
        t1 = Term("t1", -2.0, 'y', 3)  # -2y^3
        t2 = Term("t2", 4.0, 'x', 4)  # 4x^4
        t3 = Term("t3", 8.0, ' ', 0)  # 8

        l1 = Polynomial('P1')
        l1.addTerm(t0)
        l1.addTerm(t1)

        l2 = Polynomial('P2')
        l2.addTerm(t2)
        l2.addTerm(t3)
        self.polynomes = [l1, l2]

    @staticmethod
    def saisirTermes():
        termes = []
        while True:
            terme_name = input("Entrez le nom du terme (ou 'q' pour arrêter) :").strip()
            if terme_name.lower() == 'q':
                break  # Quitter la boucle si l'utilisateur entre 'q'
            try:
                variable = input("Entrez la variable du terme : ")
                coefficient = float(input("Entrez le coefficient du terme : "))
                exponent = int(input("Entrez l'exposant du terme : "))
                terme = Term(terme_name, coefficient, variable, exponent)
                termes.append(terme)
            except ZeroCoefficientException as e:
                print(f"Erreur : {e}")
            except Exception as e:
                print(f"Erreur de saisie: {e}")
        return termes

    def afficherMenu(self):
        print("********************")
        print("1 - Ajouter un polynôme")
        print("2 - Afficher tous les polynômes")
        print("3 - Simplifier un polynôme")
        print("4 - Additionner deux polynômes")
        print("5 - Trier un polynôme")
        print("6 - Sauvegarder les polynômes")
        print("7 - Charger des polynômes")
        print("0 - Quitter")
        print("********************")

    def afficherNomsPolynomesExistants(self):
        pass
        # ajouter code ici

    def saisirNomPolynome(self):
        print("Voici la liste des polynômes")
        self.afficherNomsPolynomesExistants()
        return input("Saisir le nom du polynôme: ")

    def ajoutPolynome(self):
        self.saisirNomPolynome()
        # ajouter code ici

    # ajouter code ici
    def afficherPolynomes(self):
        pass
        # ajouter code ici

    def simpilifierPolynome(self):
        pass
        self.saisirNomPolynome()
        # ajouter code ici

    def additionnerPolynomes(self):
        pass
        p1 = self.saisirNomPolynome()
        p2 = self.saisirNomPolynome()
        # ajouter code ici

    def sauvegarderPolynomes(self):
        pass
        # ajouter code ici

    def chargerPolynomes(self):
        pass
        # ajouter code ici

    def trierPolynome(self):
        pass
        # ajouter code ici

    def afficherPrompt(self):
        while True:
            self.afficherMenu()
            option = int(input("Sélectioner une option: "))

            if option == 1:
                self.ajoutPolynome()
            elif option == 2:
                self.afficherPolynomes()
            elif option == 3:
                self.simpilifierPolynome()
            elif option == 4:
                self.additionnerPolynomes()
            elif option == 5:
                self.trierPolynome()
            elif option == 6:
                self.sauvegarderPolynomes()
            elif option == 7:
                self.chargerPolynomes()
            elif option == 0:
                print("Quitter...")
                break
            else:
                print("Erreur - stop")
                break


if __name__ == "__main__":
    app = ConsoleApp()
    app.initListePolynome()
    app.afficherPrompt()
