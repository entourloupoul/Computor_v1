# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    computor.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pmasson <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/03/20 15:07:10 by pmasson           #+#    #+#              #
#    Updated: 2019/03/25 08:11:23 by pmasson          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/python3.4
import signal
import sys
import utils
from equation import Equation
import solve

signal.signal(signal.SIGINT, utils.close_prog)

def computor():
    if (len(sys.argv) != 2):
        print("wrong nb of arguments")
        print(utils.usage)
        sys.exit(0)
    else:
        equ1 = utils.check_equation(sys.argv[1])
    equ = utils.get_terms(equ1)
    equation = Equation(equ)
    print("Reduced form : {}".format(equation))
    print("Rational reduced form : {}\n".format(equation.rational()))
    print("Natural reduced form : {}".format(equation.natural()))
    print("Natural rational reduced form : {}\n".format(equation.natural_rat()))
    print("Polynomial degree = {}".format(equation.po()))
    if (equation.po() > 2):
        print("The polynomial degree is stricly greater than 2, I can't solve.")
        sys,exit(0)
    solve.def_sol(equation)



if __name__ == "__main__":
    computor()

