# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    solve.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pmasson <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/03/21 18:20:42 by pmasson           #+#    #+#              #
#    Updated: 2019/03/21 20:01:09 by pmasson          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/python3.4

import equation

def get_det(equation):
    if (equation.rat == 0):
        t0 = equation._terms[0] / equation._terms[1]
        t1 = equation._terms[2] / equation._terms[3]
        t2 = equation._terms[4] / equation._terms[5]
        det = (t1 * t1 - 4 * t0 * t2, 1)
    else:
        bn = equation._terms[2]
        bd = equation._terms[3]
        an = equation._terms[0]
        ad = equation._terms[1]
        cn = equation._terms[4]
        cd = equation._terms[5]
        det = (ad * cd * bn * bn - 4 * an * cn * bd * bd, bd * bd * ad * cd)
    return (det)

def square_root(nb):
    a = 1
    while (a * a < nb):
        a += 1
    if (a * a == nb):
        return (a)
    a = a if (a * a - nb) < (nb - (a - 1) * (a - 1)) else a - 1
    i = 0
    while (i < 10):
        a = (a + nb / a ) / 2
        i += 1
    return (a)
