#!/usr/bin/env python3
import sys
import os
from typing import List

from Tools.Polynomial import Polynomial
from Tools.Term import Term

mes_polynomes = []


def get_data(folder_path, file_name):
    entire_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), folder_path + file_name + '.polynome')

    if not os.path.exists(entire_file_path):
        print("ce fichier n'existe pas")
        sys.exit(1)

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
    return mes_polynomes
