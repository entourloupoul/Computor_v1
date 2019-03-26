# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    solve.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pmasson <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/03/21 18:20:42 by pmasson           #+#    #+#              #
#    Updated: 2019/03/22 19:48:26 by pmasson          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/python3.4

import equation

def pgcd(i, j):
    j = j if j >= 0 else -j
    i = i if i >= 0 else -i
    if (j == 0):
        return (i)
    else:
        return (pgcd(j, i % j))

def get_det(equation):
    if (equation.rat() == 0):
        t0 = equation.terms()[0] / equation.terms()[1]
        t1 = equation.terms()[2] / equation.terms()[3]
        t2 = equation.terms()[4] / equation.terms()[5]
        det = (t1 * t1 - 4 * t0 * t2, 1)
    else:
        bn = equation.terms()[2]
        bd = equation.terms()[3]
        an = equation.terms()[4]
        ad = equation.terms()[5]
        cn = equation.terms()[0]
        cd = equation.terms()[1]
        det = (ad * cd * bn * bn - 4 * an * cn * bd * bd, bd * bd * ad * cd)
    return (det)

def square_root(nb):
    a = 0
    while (a * a < nb):
        a += 1
    if (a * a == nb):
        return (a)
    a = a if (a * a - nb) < (nb - (a - 1) * (a - 1)) else a - 1
    a = a if a != 0 else 1
    i = 0
    while (i < 10):
        a = (a + nb / a ) / 2
        i += 1
    return (a)

def def_sol_31(equ, a, b, det):
    det1 = det[0] / det[1]
    rdet = square_root(det1)
    if (int(b) == b and int(a) == a):
        if (int(rdet) == rdet):
            num = -b + rdet
            den = 2 * a
            pg = pgcd(num, den)
            if (pg > 1):
                num = num / pg
                den = den / pg
            if (den < 0):
                den = -den
                num = -num
            print("Rational solution :")
            if (den != 1):
                print("X1 = {} / {}".format(int(num), int(den)))
            else:
                print("X1 = {}".format(int(num)))
            num = -b - rdet
            den = 2 * a
            pg = pgcd(num, den)
            if (pg > 1):
                num = num / pg
                den = den / pg
            if (den < 0):
                den = -den
                num = -num
            if (den != 1):
                print("X2 = {} / {}".format(int(num), int(den)))
            else:
                print("X1 = {}".format(int(num)))
        else:
            print("rational solution :")
            det2 = det[0]
            det3 = det[1]
            pg = pgcd(det2, det3)
            if (pg > 1):
                det2 = det2 / pg
                det3 = det3 / pg
            if (a != 1):
                if (det3 != 1):
                    print("X1 = ({} + ({} / {})^0.5) / {}".format(int(-b), int(det2), int(det3), int(2*a)))
                    print("X2 = ({} - ({} / {})^0.5) / {}".format(int(-b), int(det2), int(det3), int(2*a)))
                else:
                    print("X1 = ({} + ({})^0.5) / {}".format(int(-b), int(det2), int(2*a)))
                    print("X2 = ({} - ({})^0.5) / {}".format(int(-b), int(det2), int(2*a)))
            else:
                if (det3 != 1):
                    print("X1 = ({} + ({} / {})^0.5) / 2".format(int(-b), int(det2), int(det3)))
                    print("X2 = ({} - ({} / {})^0.5) / 2".format(int(-b), int(det2), int(det3)))
                else:
                    print("X1 = ({} + ({})^0.5) / 2".format(int(-b), int(det2)))
                    print("X2 = ({} - ({})^0.5) / 2".format(int(-b), int(det2)))

def def_sol_32(equ, a, b, det):
    det1 = det[0] / det[1]
    rdet = square_root(det1)
    if (int(b) == b and int(a) == a):
        if (int(rdet) == rdet):
            num = -b
            num1 = rdet
            den = 2 * a
            den1 = 2 * a
            pg = pgcd(num, den)
            if (pg > 1):
                num = num / pg
                den = den / pg
            if (den < 0):
                den = -den
                num = -num
            pg = pgcd(num1, den1)
            if (pg > 1):
                num1 = num1 / pg
                den1 = den1 / pg
            if (den1 < 0):
                den1 = -den1
                num1 = -num1
            print("Rational solution :")
            if (den != 1):
                print("X1 = {} / {}".format(int(num), int(den)),end = "")
            else:
                print("X1 = {}".format(int(num)), end="")
            if (den1 != 1):
                print(" + {} / {}".format(int(num1), int(den1)))
            else:
                print(" + {}".format(int(num1)))
            if (den != 1):
                print("X2 = {} / {}".format(int(num), int(den)), end = "")
            else:
                print("X2 = {}".format(int(num)), end="")
            if (den1 != 1):
                print(" - {} / {}".format(int(num1), int(den1)))
            else:
                print(" - {}".format(int(num1)))
        else:
            print("rational solution :")
            det2 = det[0]
            det3 = det[1]
            pg = pgcd(det2, det3)
            if (pg > 1):
                det2 = det2 / pg
                det3 = det3 / pg
            if (a != 1):
                if (det3 != 1):
                    print("X1 = ({} + i * ({} / {})^0.5) / {}".format(int(-b), int(det2), int(det3), int(2*a)))
                    print("X2 = ({} - i * ({} / {})^0.5) / {}".format(int(-b), int(det2), int(det3), int(2*a)))
                else:
                    print("X1 = ({} + i * ({})^0.5) / {}".format(int(-b), int(det2), int(2*a)))
                    print("X2 = ({} - i * ({})^0.5) / {}".format(int(-b), int(det2), int(2*a)))
            else:
                if (det3 != 1):
                    print("X1 = ({} + i * ({} / {})^0.5) / 2".format(int(-b), int(det2), int(det3)))
                    print("X2 = ({} - i * ({} / {})^0.5) / 2".format(int(-b), int(det2), int(det3)))
                else:
                    print("X1 = ({} + i * ({})^0.5) / 2".format(int(-b), int(det2)))
                    print("X2 = ({} - i * ({})^0.5) / 2".format(int(-b), int(det2)))

def def_sol_3(equ, det):
    det1 = det[0] / det[1]
    rdet = square_root(det1) if det1 >= 0 else square_root(-det1)
    b = equ.terms()[2] / equ.terms()[3]
    a = equ.terms()[4] / equ.terms()[5]
    sol1 = (-b + rdet) / (2 * a)
    sol2 = (-b - rdet) / (2 * a)
    sol1 = sol1 if int(sol1) != sol1 else int(sol1)
    sol2 = sol2 if int(sol2) != sol2 else int(sol2)
    if (det1 > 0):
        print("Discriminant strictly positive")
        print("This equation has 2 solutions on R : ")
        print("X1 = {}\nX2 = {}".format(sol1, sol2))
        def_sol_31(equ, a, b, det)
    if (det1 < 0):
        print("Discriminant strictly negative")
        print("This equation has 2 solutions on C : ")
        print("X1 = ", end="")
        if (b != 0):
            s1 = -b / a if -b / a != int(-b / a) else int(-b / a)
            print(s1, end="")
        rdet = rdet / a if rdet / a != int(rdet / a) else int(rdet / a)
        print(" + i * {}".format(rdet))
        print("X2 = ", end="")
        if (b != 0):
            print(s1, end="")
        print(" - i * {}".format(rdet))
        def_sol_32(equ, a, b, det)

def def_sol_2(equ):
    det = get_det(equ)
    det1 = det[0] / det[1]
    if (det1 == 0):
        print("Discriminant = 0")
        print("This equation has only one solution on R : \nX = ", end="")
        num = -equ.terms()[2] * equ.terms()[5]
        den = equ.terms()[3] * equ.terms()[4] * 2
        pg = pgcd(num, den)
        if (pg > 1):
            num = num / pg
            den = den / pg
        sol = num / den
        sol = int(sol) if int(sol) == sol else sol
        print(sol)
        if (equ.rat() == 1 and den != 1 and int(sol) != sol):
            print("Rational form : X = {} / {}".format(int(num), int(den)))
    else:
        def_sol_3(equ, det)


def def_sol(equ):
    if (equ.po() == 0 and equ.terms[0] != 0):
        print("This equation is false")
    elif (equ.po() == 0 and equ.terms[0] == 0):
        print("This equation is true for every X on R")
    elif (equ.po() == 1):
        num = -equ.terms()[0] * equ.terms()[3]
        den = equ.terms()[1] * equ.terms()[2]
        pg = pgcd(num, den)
        if (pg > 1):
            num = num / pg
            den = den / pg
        sol = num / den
        sol = int(sol) if int(sol) == sol else sol
        print("This equation has only one solution on R : \nX = {}".format(sol))
        if (equ.rat() == 1 and den != 1):
            print("Rational form : \nX = {} / {}".format(int(num), int(den)))
    elif (equ.po() == 2):
        def_sol_2(equ)
            


