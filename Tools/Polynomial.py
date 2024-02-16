import string
from functools import cmp_to_key
from typing import List

from Tools.Term import Term
from Tools.TermComparator import TermComparator


class Polynomial:

    # 1----------------------------------------------------------------
    def __init__(self, PolynomialName: string, TermsList: List[Term] = []):
        # TODO: exceptions should be caught

        self.PolynomialName = PolynomialName
        self.termsList = TermsList

    # 2----------------------------------------------------------------
    def addTerm(self, t: Term):
        if (self.termsList.append(t)):
            return True
        return False

    def removeTerm(self, t: Term):
        if t in self.termsList:
            self.termsList.remove(t)
            return True
        return False

    def getTermCount(self) -> int:
        return len(self.termsList)

    def getVariables(self):
        variables = []
        for t in self.termsList:
            if t.getVariable() not in variables:
                variables.append(t.getVariable())
        return variables

    def getExponents(self):
        exponents = []
        for t in self.termsList:
            if t.getVariable() not in exponents:
                exponents.append(t.getVariable())
        return exponents

    def getTerms(self, variable, exponent) -> List[Term]:
        terms = []
        for t in self.termsList:
            if t.getVariable() is variable and t.getExponent() is exponent:
                terms.append(t)
        return terms

    def getAllTerms(self) -> List[Term]:
        return self.termsList

    def sort(self):
        sorted_terms = sorted(self.termsList, key=cmp_to_key(lambda t1, t2: TermComparator.compare(t1, t2)))
        print(sorted_terms)
        return self.__init__('sorted Polynomial', sorted_terms)


    def __str__(self):
        return ("+".join(str(t) for t in self.termsList)).replace("+-", "-")


if __name__ == "__main__":
    # pol = Polynomial('test', ['2x^3', '4y', '-5x', '6'])
    # term = Term('test', 2, "x", 3)
    # print(term.__str__())   #or print(str(term)). it is same thing
    # print(pol.getVariables())
    TermComparator.compare_lengths('toto', 'tot')
