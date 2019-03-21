# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    utils.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pmasson <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/03/20 15:01:01 by pmasson           #+#    #+#              #
#    Updated: 2019/03/21 20:01:11 by pmasson          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/python3.4

import sys
import re

usage = "usage : ./computor.py \"equation\""
input_format = r"^[0-9+-=*/X^]{1,}$"
is_doub = r"^[0-9]{1,}.?[0-9]*$"

def close_prog(signal, frame):
    sys.exit(0)

def check_equation(equation):
    """checks the format of the equation"""
    equation = equation.replace(" ", "")
    equation = equation.upper()
    if (re.search(input_format, equation) == None):
        print("Error, wrong characters in equation")
        sys.exit(0)
    if (equation.count("=") != 1):
        print("Error, wrong number of \"=\" in equation")
        sys.exit(0)
    equation = equation.replace("+", " +")
    equation = equation.replace("^ +", "^+")
    equation = equation.replace("-", " -")
    equation = equation.replace("^ -", "^-")
    equation = equation.replace("=", " = ")
    equation = equation.replace("  ", " ")
    if (len(equation) > 0):
        if (equation[0] == " "):
            equation = equation[1:]
    return (equation)

def get_po(elt):
    po = 0
    if (len(elt) == 1):
        return (1)
    else:
        if (len(elt) < 3 or elt[1] != "^"):
            print("Error, wrong format in X terms")
            sys.exit(0)
        try:
            po = int(elt[2:])
        except ValueError:
            print("Error, wrong format in X terms")
            sys.exit(0)
    return (po)


def manage_equation_terms(equ, eqsp1, b, sign):
    num = 1
    den = 1
    po = 0
    op = 0
    for i, elt in enumerate(eqsp1):
        if (re.search(is_doub, elt) != None):
            if (op == 0 or op == 1):
                num = num * float(elt)
            else:
                den = den * float(elt)
                if (den == 0):
                    print("Error, division by 0")
                    sys.exit(0)
            op = 0
        elif (elt.count("X") == 1):
            deg = get_po(elt)
            po = po + deg if op == 0 or op == 1 else po - deg
            op = 0
        else :
            op = 1 if elt == "*" else 2
    j = len(equ)
    while (j <= 2 * po + 1):
        equ.append(0)
        equ.append(1)
        j += 2
    equ[2 * po] = equ[2 * po] * den + num * b * sign * equ[2 * po + 1]
    equ[2 * po + 1] *= den
    return (equ)

def check_equation_terms(equ, eqsp, b):
    sign = -1 if eqsp[0] == "-" else 1
    if (eqsp[0] == "-" or eqsp[0] == "+"):
        eqsp = eqsp[1:]
    eqsp = eqsp.replace("*", " * ")
    eqsp = eqsp.replace("/", " / ")
    eqsp = eqsp.replace(",", ".")
    eqsp1 = eqsp.split(" ")
    i = 0
    while (i < len(eqsp1)):
        if (re.search(is_doub, eqsp1[i]) == None and eqsp1[i].count("X") != 1):
            print("Error, wrong format in terms")
            sys.exit(0)
        i += 1
        if (i < len(eqsp1) and eqsp1[i] != "/" and eqsp1[i] != "*"):
            print("Error, wrong format in terms")
            sys.exit(0)
        i += 1
    return (manage_equation_terms(equ, eqsp1, b, sign))

def get_terms(equation):
    equ = list()
    equation1 = equation.split(" ")
    if (len(equation1) == 0):
        print("Error, no expression")   
        sys.exit(0)
    i = 0
    b = 1
    while (i < len(equation1)):
        if (equation1[i] == "="):
            b = -1
        else:
            equ = check_equation_terms(equ, equation1[i], b)
        i += 1
    return (equ)
