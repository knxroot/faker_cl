#!/usr/bin/python
# -*- coding: utf-8 -*-
""" A simple Faker Chilean Phone Provider """

__author__ = "Gustavo Lacoste"

from faker.providers import BaseProvider

class ChileanPhone(BaseProvider):

    def cl_mobile_phone(self, explode=False):
        """Return a valid Chilean mobile phone"""

        tpl = ('{start_digit}{mobile_8digits}')

        start_digit = self.random_element(('9', '8', '7', '6'))
        mobile_8digits = self.numerify("#######")

        tpl = tpl.format(start_digit = start_digit,
                         mobile_8digits = self.numerify("#######"))
        mobile_phone_full = self.generator.parse(tpl)

        return ((56, 9, mobile_phone_full) if explode else '+56 9 '+mobile_phone_full)

    def cl_land_phone(self, explode=False):
        """Return a valid Chilean land line phone"""

        tpl = ('+56 {area_prefix} {local_number}')

        area_prefix = str(self.random_element((2, 32, 33, 34, 35, 39, 41, 42, 43, 44, 45, 51, 52, 53, 55, 57, 58, 61, 63, 64, 65, 67, 68, 71, 72, 73, 75))).strip()

        local_number = self.numerify('2######')

        if area_prefix == '2':
            local_number = self.numerify('2#######')

        tpl = tpl.format(area_prefix = area_prefix,
                         local_number = local_number)

        land_phone_full = self.generator.parse(tpl)
        return ((56, area_prefix, local_number) if explode else land_phone_full)