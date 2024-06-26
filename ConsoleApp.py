import os
import sys

from Exceptions.ZeroCoefficientException import ZeroCoefficientException
from Tools.Polynomial import Polynomial
from Tools.PolynomialToolbox import PolynomialToolbox
from Tools.Term import Term
from Tools.Utils import Utils
from charger import get_data


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
        for polynom in self.polynomes:
            print(polynom.PolynomialName)


    def saisirNomPolynome(self):
        print("Voici la liste des polynômes")
        self.afficherNomsPolynomesExistants()
        return input("Saisir le nom du polynôme: ")


    #new: check if polynome with this name exists
    def getPolynomeByName(self, name):
        res = list(filter(lambda x: x.PolynomialName == name, self.polynomes))
        return res[0] if len(res) else None

    def ajoutPolynome(self):
        nom = self.saisirNomPolynome()
        while self.getPolynomeByName(nom) is not None:
            print("un polynome avec ce nom existe deja")
            nom = self.saisirNomPolynome()

        termes = self.saisirTermes()
        self.polynomes.append(Polynomial(nom, termes))


    def afficherPolynomes(self):
        for polynom in self.polynomes:
            print(str(polynom))


    def simpilifierPolynome(self):
        nom = self.saisirNomPolynome()
        polynome = self.getPolynomeByName(nom)
        if polynome is None:
            return
        return PolynomialToolbox.simplify(polynome)

    def additionnerPolynomes(self):
        p1 = self.getPolynomeByName(self.saisirNomPolynome())
        if p1 is None:
            print("Verifiez bien que ce polynome existe dans la liste")
            return

        p2 = self.getPolynomeByName(self.saisirNomPolynome())
        if p2 is None:
            print("Verifiez bien que ce polynome existe dans la liste")
            return

        return PolynomialToolbox.sum(self.getPolynomeByName(p1), self.getPolynomeByName(p2))


    def sauvegarderPolynomes(self):
        print("Entrez le chemin_dossier :")
        folder = input()
        if folder is None:
            print("Le chemin du dossier est obligatoire")
            return
        if folder[-1] != '/':
            print("Le chemin du dossier est incorrect. Le chemin du dossier doit finir par /")
            return

        print("Entrez le nom du fichier :")
        filename = input()
        if filename is None:
            print("Le nom du fichier a creer est obligatoire")

        sauvegarder_script_path = os.path.abspath("sauvegarder.py")
        # `sudo chmod +x sauvegarder.py`

        Utils.addToPathIfNotExists(sauvegarder_script_path)

        texte = ''
        for polynom in self.polynomes:
            poly_lines = polynom.PolynomialName + ';'
            for term in polynom.getAllTerms():
                poly_lines += "{},{},{},{}".format(term.TermName, term.getCoefficient(), term.getVariable(), term.getExponent()) + ';'
            texte += poly_lines + ';'

        # print(texte)
        os.system('{} {} {} "{}"'.format(sauvegarder_script_path, folder, filename, texte))
        print("sauvegarde en cours...")


    def chargerPolynomes(self):
        print("Entrez le chemin_dossier (example docs/):")
        folder = input()
        if folder is None:
            print("Le chemin du dossier est obligatoire")
            return
        if folder[-1] != '/':
            print("Le chemin du dossier est incorrect. Le chemin du dossier doit finir par /")
            return

        print("Entrez le nom du fichier :")
        filename = input()
        if filename is None:
            print("Le nom du fichier a creer est obligatoire")

        self.polynomes = []

        print("=======Chargement en cours==========")
        self.polynomes = get_data(folder, filename)
        print("=========Chargement fini========")
        self.afficherPolynomes()



    def trierPolynome(self):
        nom = self.saisirNomPolynome()
        polynome = self.getPolynomeByName(nom)
        if polynome is None:
            print("Aucun polynome de ce nom")
            return
        print(str(polynome), 'avant')
        polynome.sort()
        print(str(polynome), 'apres')


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
