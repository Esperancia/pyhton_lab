from ..Exceptions.ZeroCoefficientException import ZeroCoefficientException

# 1----------------------------------------------------------------
class Term:
    TermName = None

# 2----------------------------------------------------------------
    def __init__(self, TermName, Coefficient, Variable, Exponent):
        # TODO: exceptions should be caught
        
        if Coefficient is None or Coefficient == "":
            raise ZeroCoefficientException("Terms with a zero coeffcient are invalid")
        
        self.TermName = TermName
        self.__coefficient = Coefficient
        self.__variable = Variable
        self.__exponent = Exponent
        
# 3----------------------------------------------------------------
    def getCoefficient(self):
        return round(self.__coefficient,1)
    
    def getVariable(self):
        return self.__variable
    
    def getExponent(self):
        return self.__exponent
    
# 4----------------------------------------------------------------
    def __str__(self):
        if self.__variable in [None, ""] or self.__exponent in [None, 0, ""]:
            return f"{self.__coefficient}"
        else:
            return f"{self.__coefficient}{self.__variable}^{self.__exponent}"


if __name__ == '__main__':
    print(__package__)