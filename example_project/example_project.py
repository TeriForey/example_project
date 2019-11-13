# -*- coding: utf-8 -*-
import numpy as np


def fahrToKelv(temp):
    """
    takes a temperature `temp` in fahrenheit and returns it in Kelvin
    """

    kelvin = 5./9. * (temp - 32.) + 373.15

    return kelvin
