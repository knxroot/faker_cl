#!/usr/bin/python
# -*- coding: utf-8 -*-
""" A simple Faker Chilean Rut Provider """

__author__ = "Gustavo Lacoste"

from faker.providers import BaseProvider
import random
from itertools import cycle

class ChileanRut(BaseProvider):

    def cl_rut(self, explode=False):
        """Return a full rut with check digit"""
        tpl = ('{number}-{check_digit}')

        int_rut_number = int(round(random.random()*(25000000-5000000))+5000000)
        str_dv = self._generate_dv(int_rut_number)

        tpl = tpl.format(number = int_rut_number,
                         check_digit = str_dv)
        
        rut_full = self.generator.parse(tpl)

        return ((int_rut_number, str_dv) if explode else rut_full)

    @classmethod
    def _generate_dv(self, rut_number):
        """ Return a valid check digit (as String) for the number
        if check digit if 10 then 'K' character is returned """

        str_rndrut = str(rut_number)
        # Making the dv for the random number
        reversed_digits = map(int, reversed(str_rndrut))
        factors = cycle(range(2, 8))
        s = sum(d * f for d, f in zip(reversed_digits, factors))
        dv = (-s) % 11
        str_dv = ('K' if dv == 10 else str(dv))
        return str_dv