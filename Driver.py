from Tools.Polynomial import Polynomial
from Tools.PolynomialToolbox import PolynomialToolbox
from Tools.Term import Term


class Driver:

    t0 = Term("t0", 3.0, 'x', 2) # 3x^2
    t1 = Term("t1", -2.0, 'y', 3) # -2y^3
    t2 = Term("t2", 4.0, 'x', 4) # 4x^4
    t3 = Term("t3", 8.0, ' ', 0) # 8
    l1 = Polynomial('P1')

    print("Ajout de t0 dans l1:", l1.addTerm(t0))
    print("Ajout de t1 dans l1:", l1.addTerm(t1))


    t4 = Term("t0", 7.0, 'x', 2) # 7x^2
    print("Ajout de t0 dans l1:", l1.addTerm(t3))
    print("Ajout de t1 dans l1:", l1.addTerm(t2))



    print("Termes dans l1:", [str(term) for term in l1.getAllTerms()])
    print("Exposants dans l1:", l1.getExponents())

    print("Termes avec la variable 'x' et exposant 2 dans l1:", [str(term) for term in l1.getTerms('x', 2)])
    print("Variables dans l1:", l1.getVariables())
    print("Polynôme l1:", l1)

    print("Simplification de l1:", PolynomialToolbox.simplify(l1))
    l2 = Polynomial('P2')
    print("Termes dans l2:", [str(term) for term in l2.getAllTerms()])
    print("Ajout de t2 dans l2:", l2.addTerm(t2))
    print("Ajout de t3 dans l2:", l2.addTerm(t3))
    print("Polynôme l2:", l2)
    l3 = PolynomialToolbox.sum(l1, l2)
    print("Somme de l1 et l2 :", l3)
    l3.sort()
    print("Somme de l1 et l2 triée :", l3)
