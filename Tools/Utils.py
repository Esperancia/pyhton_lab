from functools import cmp_to_key


class Utils:

    # Fonction de comparaison pour le tri
    @staticmethod
    def compare_lengths(str1, str2):
        if len(str1) < len(str2):
            return -1
        elif len(str1) == len(str2):
            return 0
        else:
            return 1
        #Liste de chaînes de caractères à trier
        strings = ["banana", "apple", "orange", "kiwi"]
        # Tri de la liste en utilisant cmp_to_key avec la fonction de comparaison
        sorted_strings = sorted(strings, key=cmp_to_key(compare_lengths))
        # Affichage du résultat du tri
