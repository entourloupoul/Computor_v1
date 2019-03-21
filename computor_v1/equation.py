# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    equation.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pmasson <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/03/20 16:19:34 by pmasson           #+#    #+#              #
#    Updated: 2019/03/21 18:20:29 by pmasson          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/python3.4

class   Equation():
    """class containing each parameter of the equation, the max power..."""

    def __init__(self, equ):
        self._terms = list(equ)
        i = 0
        self._rat = 1
        while (i < len(self._terms)):
            a = int(self._terms[i])
            if (a != self._terms[i]):
                self._rat = 0
            i += 1
        j = len(self._terms)
        while (j < 6):
            self._terms.append(0)
            j += 1
        i = 0
        po = 0
        while (i < len(self._terms)):
            po = i / 2 if self._terms[i] != 0 else po
            i += 2
        self._po = int(po)

    def __repr__(self):
        ret = str()
        i = 0
        while (i <= 2 * self._po):
            nb = self._terms[i] / self._terms[i + 1]
            a = int(nb)
            a = a if a == nb else nb
            if (i == 0):
                ret += str(a)
            if (i >= 2):
                if (self._terms[i] < 0):
                    ret += " - "
                    ret += str(-a)
                else:
                    ret += " + "
                    ret += str(a)
            ret += " * "
            ret += "X^{}".format(int(i / 2))
            i += 2
        ret += " = 0"
        return (ret)

    def __str__(self):
        return (repr(self))

    def rational(self):
        ret = str()
        if (self._rat == 0):
            return ("rational form not possible")
        i = 0
        while (i <= 2 * self._po):
            if (i == 0):
                ret += str(int(self._terms[i]))
                if (self._terms[i + 1] != 1):
                    ret += "/{}".format(str(int(self._terms[i + 1])))
            if (i >= 2):
                if (self._terms[i] < 0):
                    ret += " - "
                    ret += str(int(-self._terms[i]))
                    if (self._terms[i + 1] != 1):
                        ret += "/{}".format(str(int(self._terms[i + 1])))
                else:
                    ret += " + "
                    ret += str(int(self._terms[i]))
                    if (self._terms[i + 1] != 1):
                        ret += "/{}".format(str(int(self._terms[i + 1])))
            ret += " * "
            ret += "X^{}".format(int(i / 2))
            i += 2
        ret += " = 0"
        return (ret)
    
    def natural_rat(self):
        ret = str()
        if (self._rat == 0):
            return ("rational form not possible")
        i = 0
        while (i <= 2 * self._po):
            nb = self._terms[i] / self._terms[i + 1]
            if (i == 0):
                if (nb != 0 and nb != 1):
                    ret += str(int(self._terms[i]))
                    if (self._terms[i + 1] != 1):
                        ret += "/{}".format(str(int(self._terms[i + 1])))
            if (i >= 2):
                if (nb != 0 and nb != 1):
                    if (self._terms[i] < 0):
                        ret = ret + " - " if len(ret) > 0 else ret + "-"
                        ret += str(int(-self._terms[i]))
                        if (self._terms[i + 1] != 1):
                            ret += "/{}".format(str(int(self._terms[i + 1])))
                    else:
                        ret = ret + " + " if len(ret) > 0 else ret
                        ret += str(int(self._terms[i]))
                        if (self._terms[i + 1] != 1):
                            ret += "/{}".format(str(int(self._terms[i + 1])))
            if (nb != 0):
                if (nb == 1 and len(ret) > 0):
                    ret += " + "
                elif (i > 0 and len(ret) > 0):
                    ret += " * "
                if (i == 2):
                    ret += "X"
                if (i > 2):
                     ret += "X^{}".format(int(i / 2))
            i += 2
        if (len(ret) == 0):
            ret += "0"
        ret += " = 0"
        return (ret)
    
    def natural(self):
        ret = str()
        i = 0
        while (i <= 2 * self._po):
            nb = self._terms[i] / self._terms[i + 1]
            a = int(nb)
            nb = nb if a != nb else a
            if (i == 0):
                if (nb != 0 and nb != 1):
                    ret += str(nb)
            if (i >= 2):
                if (nb != 0 and nb != 1):
                    if (self._terms[i] < 0):
                        ret = ret + " - " if len(ret) > 0 else ret + "-"
                        ret += str(-nb)
                    else:
                        ret = ret + " + " if len(ret) > 0 else ret
                        ret += str(nb)
            if (nb != 0):
                if (nb == 1 and len(ret) > 0):
                    ret += " + "
                elif (i > 0 and len(ret) > 0):
                    ret += " * "
                if (i == 2):
                    ret += "X"
                if (i > 2):
                     ret += "X^{}".format(int(i / 2))
            i += 2
        if (len(ret) == 0):
            ret += "0"
        ret += " = 0"
        return (ret)

    def po(self):
        return (self._po) 



