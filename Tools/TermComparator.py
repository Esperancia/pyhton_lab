from functools import cmp_to_key

from Tools.Term import Term


# 1-------------------------------------------------------------
class TermComparator:

    # Fonction de comparaison pour le tri
    @staticmethod
    def compare_lengths(str1, str2):
        if len(str1) < len(str2):
            return -1
        elif len(str1) == len(str2):
            return 0
        else:
            return 1

# 2- ------------------------------------------------------------
    def compare(self, t1: Term, t2: Term):
        variable_t1 = t1.getVariable()
        variable_t2 = t2.getVariable()
        if variable_t1 == '' or variable_t1 > variable_t2:
            return 1
        if variable_t2 == '' or variable_t1 < variable_t2:
            return -1
        if variable_t2 == variable_t1:
            return 1 if (t1.getExponent() > t2.getExponent()) else -1
        return 0


# test exemple methode de comparaison
if __name__ == "__main__":
    #Liste de chaînes de caractères à trier
    strings = ["banana", "apple", "orange", "kiwi", "mango"]
    # Tri de la liste en utilisant cmp_to_key avec la fonction de comparaison
    sorted_strings = sorted(strings, key=cmp_to_key(TermComparator.compare_lengths))
    # Affichage du résultat du tri
    print("Liste triée par longueur des chaînes de caractères:", sorted_strings)
