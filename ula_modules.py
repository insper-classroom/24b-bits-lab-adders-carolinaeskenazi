#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

from myhdl import *


@block
def halfAdder(a, b, soma, carry):
    @always_comb
    def comb():
        soma.next = a ^b
        carry.next = a and b

    return instances()


@block
def fullAdder(a, b, c, soma, carry):
    s = [Signal(bool(0)) for i in range(3)]

    half_1 = halfAdder(a, b, s[0], s[1]) 
    half_2 = halfAdder(c, s[0], soma, s[2])

    @always_comb
    def comb():
        carry.next = s[1] | s[2]

    return instances()

@block
def adder2bits(x, y, soma, carry):
    vaium = Signal(bool(0))
    s1 = halfAdder(x[0],y[0],soma[0],vaium)
    s2 = fullAdder(x[1],y[1],vaium,soma[1],carry)
    

    return instances()


@block
def adder(x, y, soma, carry):
    @always_comb
    def comb():
        pass

    return instances()

