"""
Implémentez une fonction en Python qui utilise le module sched pour planifier une tâche
de simplification périodique des polynômes dans notre application de gestion. Planifiez
cette tâche pour qu'elle s'exécute chaque dix minutes. La fonction doit commencer par
charger les polynômes stockés dans un fichier dont le nom et le chemin sont des
paramètres à passer au programme. Le chargement doit s’effectuer tel qu’expliqué
auparavant. Le résultat de simplification doit s’enregistrer dans un fichier ayant le même
le nom du fichier entré en paramètre avec un suffix ‘_simplife’. Par exemple, si le nom du
fichier est égal ‘polynomes.polynome’ la fichier résultat doit être
‘polynomes_simplifie.polynome’.
"""
import os
import sched
import time

from ConsoleApp import ConsoleApp
from Tools.Polynomial import Polynomial
from Tools.PolynomialToolbox import PolynomialToolbox
from Tools.Term import Term


def traiter_polynomes():
    print("====================Task traiter_polynomes!==========================")

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

    entire_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), folder + filename + '.polynome')

    if not os.path.exists(entire_file_path):
        print("ce fichier n'existe pas")
        return

    mes_polynomes = []

    with open(entire_file_path, "r") as file_content:
        tmp_polynomes = file_content.read().split("\n\n")
        for p in tmp_polynomes:
            tmp_polynom = p.split("\n")
            polynome_name = tmp_polynom[0]
            polynome_terms = []

            for t in tmp_polynom[1:]:
                tmp_term = t.split(',')
                term_name = tmp_term[0]
                term_coefficient = float(tmp_term[1])
                term_variable = tmp_term[2]
                term_exponent = int(tmp_term[3])
                polynome_terms.append(Term(term_name, term_coefficient, term_variable, term_exponent))

            mes_polynomes.append(Polynomial(PolynomialName=polynome_name, TermsList=polynome_terms))

    for polynome in mes_polynomes:
        old_name = polynome.PolynomialName
        new_polynome = PolynomialToolbox.simplify(polynome)

        texte = ''
        poly_lines = old_name + '_' + new_polynome.PolynomialName + ';'
        for term in new_polynome.getAllTerms():
            poly_lines += "{},{},{},{}".format(term.TermName, term.getCoefficient(), term.getVariable(), term.getExponent()) + ';'
        texte += poly_lines + ';;'

        print(texte)
        sauvegarder_script_path = os.path.abspath("sauvegarder.py")

        os.system('{} {} {} "{}"'.format(sauvegarder_script_path, folder, filename + '_simplife', texte))


scheduler = sched.scheduler(time.time, time.sleep)

scheduler.enter(600, 1, traiter_polynomes, ())

scheduler.run()
