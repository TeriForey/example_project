# -*- coding: utf-8 -*-
import numpy as np


def fahrToKelv(temp):
    """
    takes a temperature `temp` in fahrenheit and returns it in Kelvin
    """

    kelvin = 5./9. * (temp - 32.) + 273.15

    return kelvin

def KelvTofahr(temp):
    """
    takes a temperature `temp` in Kelvin and returns fahrenheit 
    """
    
    fahr = (temp + 32.) * 9/5. - 273.15


    return fahr
