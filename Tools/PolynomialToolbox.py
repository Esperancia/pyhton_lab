from collections import defaultdict
from itertools import groupby
from typing import List

from Tools.Polynomial import Polynomial
from Tools.Term import Term


class PolynomialToolbox:
    @classmethod
    def simplify(cls, l1) -> Polynomial:
        l1.sort()

        termesPolynome: List[Term] = l1.getAllTerms()
        termesNouveauPolynome: List[Term] = []

        groups = [k for k, g in groupby(termesPolynome, lambda x: x.getVariable() + '^' + str(x.getExponent()))]
        my_dict = {}

        for group in groups:
            tmp_list = []
            for obj in termesPolynome:
                if group == obj.getVariable() + '^' + str(obj.getExponent()):
                    tmp_list.append(obj)
            my_dict[group] = tmp_list

        for (group, glist) in my_dict.items():
            sommeCoef = sum(term.getCoefficient() for term in glist)
            tmp_index = list(my_dict.keys()).index(group)
            if sommeCoef != 0:
                variable = glist[0].getVariable()
                exponent = glist[0].getExponent()
                # nom = glist[0].TermName # <-----ici
                nom = "t{}".format(tmp_index)
                termesNouveauPolynome.append(Term(nom, sommeCoef, variable, exponent))

        newL1 = Polynomial('simplified', termesNouveauPolynome)
        if l1.__str__() == newL1.__str__():
            print("Le polynome ne peut pas etre plus simplifie.")
        print(newL1.__str__())
        return newL1


    @classmethod
    def sum(cls, l1: Polynomial, l2: Polynomial) -> Polynomial:
        tmp_res = [*l1.getAllTerms(), *l2.getAllTerms()]
        # for term in tmp_res:
            # print(term.__str__())
        res = Polynomial('resultat_sum', tmp_res)
        return cls.simplify(res)

