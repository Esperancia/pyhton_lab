import Term
import Utils

class Polynomial:

# 1----------------------------------------------------------------
    def __init__(self, PolynomialName, TermsList:Term = []):
        # TODO: exceptions should be caught
        
        self.PolynomialName = PolynomialName
        self.termsList = TermsList
        
# 2----------------------------------------------------------------
    def addTerm(self, t:Term):
        if (self.termsList.append(t)):
            return True
        return False


    def removeTerm(self, t:Term):
        if (t.lower() in [x.lower() for x in self.termsList]):
            self.termsList.remove(t)
            return True
        return False


    def getTermCount(self):
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


    def getTerms(self, variable, exponent):
        pass


    def getAllTerms(self):
        pass

    def sort(self):
        pass


    def __str__(self):
        return ("+".join(str(t) for t in self.termsList)).replace("+-", "-")



if __name__ == "__main__":
    pol = Polynomial('test', ['2x^3', '4y', '-5x', '6'])
    #term = Term('test', 2, "x", 3)
    #print(term.__str__())   #or print(str(term)). it is same thing
    #print(pol.getVariables())
    Utils.compare_lengths('toto', 'tot')