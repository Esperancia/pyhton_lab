from collections import defaultdict
from itertools import groupby
from typing import List

from Tools.Polynomial import Polynomial
from Tools.Term import Term


class PolynomialToolbox:
    @classmethod
    def simplify(cls, l1) -> Polynomial:
        '''
        new_l1 = Polynomial('forme_simplifiee', [])
        for t in l1.getAllTerms():
            variable = t.getVariable()
            coefficient = t.getCoefficient()
            exponent = t.getExponent()
            tmp_coefficient = []
            if
        '========'
        d = defaultdict(l1.getAllTerms())
        print(d)
        for t in tmp_list:
           # d[t.getVariable()].append(i)
            print(t)
        '''
        tmp_list = []

        '''
        for term, variable_exponent in groupby(l1.getAllTerms(), lambda x: x.getVariable() + '' + str(x.getExponent())):
            for item in variable_exponent:
                print(item)
                tmp_list.append(item.getCoefficient())
            print("")
        '''

        #tmp_list = [k for k, g in groupby(l1.getAllTerms(), lambda x: x.getVariable() + '^' + str(x.getExponent()))]
        #print(tmp_list)

        for k, g in groupby(l1.getAllTerms(), lambda x: x.getVariable() + '^' + str(x.getExponent())):
            print("key: '{}'--> group: {}".format(k, list(g)))

        return Polynomial('forme_simplifiee', tmp_list)

    @classmethod
    def sum(cls, l1: Polynomial, l2: Polynomial) -> Polynomial:
        tmp_res = [*l1.getAllTerms(), *l2.getAllTerms()]
        res = Polynomial('resultat_sum', tmp_res)
        return cls.simplify(res)

    @classmethod
    def sort(cls):
        pass
